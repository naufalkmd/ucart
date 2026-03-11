from machine import I2C, Pin
import time

RTC_ADDR = 0x68
PIN_PRESENT_N = 2
PIN_ID0 = 3
PIN_ID1 = 6
I2C_SDA = 16
I2C_SCL = 17


def bcd_to_dec(value):
    return ((value >> 4) * 10) + (value & 0x0F)


class DS1307:
    def __init__(self, i2c, address=RTC_ADDR):
        self.i2c = i2c
        self.address = address

    def present(self):
        return self.address in self.i2c.scan()

    def read_iso8601(self):
        data = self.i2c.readfrom_mem(self.address, 0x00, 7)
        second = bcd_to_dec(data[0] & 0x7F)
        minute = bcd_to_dec(data[1] & 0x7F)
        hour = bcd_to_dec(data[2] & 0x3F)
        day = bcd_to_dec(data[4] & 0x3F)
        month = bcd_to_dec(data[5] & 0x1F)
        year = 2000 + bcd_to_dec(data[6])
        return "%04d-%02d-%02dT%02d:%02d:%02dZ" % (
            year,
            month,
            day,
            hour,
            minute,
            second,
        )


class MockGnssFeed:
    def __init__(self):
        self.lines = [
            "$GPRMC,092751.000,A,5321.6802,N,00630.3372,W,0.06,31.66,280511,,,A*43",
            "$GPRMC,092752.000,V,0000.0000,N,00000.0000,E,0.00,0.00,280511,,,N*48",
            "$GPRMC,bad,line",
            "garbage",
        ]
        self.index = 0

    def next_line(self):
        line = self.lines[self.index % len(self.lines)]
        self.index += 1
        return line


def parse_gnss_line(line):
    result = {
        "seen": 0,
        "fix_mock": 0,
        "kind": "none",
        "raw": line,
    }

    if not line.startswith("$"):
        result["kind"] = "invalid"
        return result

    parts = line.split(",")
    sentence = parts[0][1:]
    result["seen"] = 1
    result["kind"] = sentence or "unknown"

    if sentence.endswith("RMC") and len(parts) > 2:
        result["fix_mock"] = 1 if parts[2] == "A" else 0

    return result


def read_present_state(present_pin):
    return 1 if present_pin.value() == 0 else 0


def read_id_bits(id0_pin, id1_pin):
    return id0_pin.value(), id1_pin.value()


def print_status(present, id0, id1, rtc_ok, rtc_time, gnss_state):
    print(
        "status "
        "present=%d id0=%d id1=%d rtc_ok=%d rtc_addr=0x%02X rtc_time=%s "
        "gnss_seen=%d gnss_fix_mock=%d gnss_kind=%s gnss_source=mock" % (
            present,
            id0,
            id1,
            rtc_ok,
            RTC_ADDR,
            rtc_time,
            gnss_state["seen"],
            gnss_state["fix_mock"],
            gnss_state["kind"],
        )
    )


present_pin = Pin(PIN_PRESENT_N, Pin.IN)
id0_pin = Pin(PIN_ID0, Pin.IN)
id1_pin = Pin(PIN_ID1, Pin.IN)
i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=100000)
rtc = DS1307(i2c)
gnss = MockGnssFeed()

print("uCart C1-001 Utility Nav Wokwi starter")
print("pins present_n=GP2 id0=GP3 id1=GP6 i2c=GP16/GP17")
print("present switch is active-low: left=present, right=absent")

last_status_ms = time.ticks_ms()
last_gnss_ms = time.ticks_ms()
gnss_state = {"seen": 0, "fix_mock": 0, "kind": "idle", "raw": ""}

while True:
    now = time.ticks_ms()
    present = read_present_state(present_pin)
    id0, id1 = read_id_bits(id0_pin, id1_pin)

    rtc_ok = 0
    rtc_time = "not-present"

    if present:
        if rtc.present():
            rtc_ok = 1
            try:
                rtc_time = rtc.read_iso8601()
            except Exception as exc:
                rtc_time = "read-error:%s" % exc

        if time.ticks_diff(now, last_gnss_ms) >= 1500:
            gnss_state = parse_gnss_line(gnss.next_line())
            print("gnss raw=%s" % gnss_state["raw"])
            last_gnss_ms = now
    else:
        gnss_state = {"seen": 0, "fix_mock": 0, "kind": "idle", "raw": ""}

    if time.ticks_diff(now, last_status_ms) >= 2000:
        print_status(present, id0, id1, rtc_ok, rtc_time, gnss_state)
        last_status_ms = now

    time.sleep_ms(100)
