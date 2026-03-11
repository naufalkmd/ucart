# C1 Utility Nav Wokwi Starter

This is the first simulation-only starter for `C1-001 Utility Nav`.

## What It Proves

- active-low cartridge present handling on `GP2`
- cartridge ID bits on `GP3` and `GP6`
- `I2C` bring-up on `GP16` and `GP17`
- basic `RTC` probing and time read flow
- mocked `GNSS` parser behavior without any RF or real receiver hardware

## What It Does Not Prove

- `RTL-SDR` or `Proxmark3` USB behavior
- real GNSS reception
- cartridge power integrity
- hot-swap behavior
- final hardware pin choices

## Wokwi Controls

- top slide switch: `present_n`
  - left = asserted low = cartridge present
  - right = deasserted = cartridge absent
- middle slide switch: `id0`
  - left = `0`
  - right = `1`
- bottom slide switch: `id1`
  - left = `0`
  - right = `1`

Default state:

- present = inserted
- id0 = `0`
- id1 = `1`

## Console Output

The project prints a compact status line every two seconds, for example:

```text
status present=1 id0=0 id1=1 rtc_ok=1 rtc_addr=0x68 rtc_time=2026-03-11T00:00:02Z gnss_seen=1 gnss_fix_mock=1 gnss_kind=GPRMC gnss_source=mock
```

## Notes

The `DS1307` is used here as a simulation stand-in because Wokwi currently supports the Pi Pico `RP2040` and `DS1307 RTC` directly, and MicroPython projects run from `main.py` with a `diagram.json` circuit description.
