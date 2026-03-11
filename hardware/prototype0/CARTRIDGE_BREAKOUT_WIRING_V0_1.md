# Cartridge Breakout Wiring v0.1

## Purpose

Define the concrete wiring layout for the Prototype 0 cartridge breakout board.

This board is the temporary electrical stand-in for an inserted `uCart` cartridge.

## Board Role

The cartridge breakout board must do three jobs cleanly:

- terminate the temporary host harness from the host breakout
- expose low-speed headers for the native `C1-001 Utility Nav` surrogate
- expose a `USB` device connection path for `C3` compatibility targets

## Functional Block Diagram

```text
From host breakout J3
        |
        +-- +5V_MAIN -----------------------------> cartridge power rail
        +-- +3V3_AUX -----------------------------> native low-speed rail
        +-- GND ----------------------------------> shared ground
        +-- UART_TX_HOST -------------------------> RP2040 surrogate RX
        +-- UART_RX_HOST <------------------------- RP2040 surrogate TX
        +-- I2C_SDA <-----------------------------> GNSS / RTC headers
        +-- I2C_SCL <-----------------------------> GNSS / RTC headers
        +-- CART_ID0 <---------------------------- strap block
        +-- CART_ID1 <---------------------------- strap block
        +-- CART_PRESENT_N <---------------------- present jumper or switch

From host breakout J4
        |
        +-- USB_D+ -------------------------------> USB device connector
        +-- USB_D- -------------------------------> USB device connector
        +-- GND ----------------------------------> USB device connector ground
        +-- optional +5V convenience ------------> USB VBUS only if required
```

## Recommended Connectors

### J1: Low-Speed and Power Harness Input

This mates with the host breakout low-speed header.

Use the same pin order as the host board.

| Pin | Signal |
| --- | ------ |
| 1 | `+5V_MAIN` |
| 2 | `+5V_MAIN` |
| 3 | `GND` |
| 4 | `+3V3_AUX` |
| 5 | `UART_TX_HOST` |
| 6 | `UART_RX_HOST` |
| 7 | `I2C_SDA` |
| 8 | `I2C_SCL` |
| 9 | `CART_ID0` |
| 10 | `CART_ID1` |
| 11 | `CART_PRESENT_N` |
| 12 | `GND` |

### J2: Dedicated USB Link Input

This mates with the host breakout USB header.

| Pin | Signal |
| --- | ------ |
| 1 | `USB_D-` |
| 2 | `USB_D+` |
| 3 | `GND` |
| 4 | optional `+5V_MAIN` convenience pass-through |

### J3: Native UART Header

Expose a simple native controller header.

Recommended signals:

- `+3V3_AUX`
- `GND`
- `UART_TX_HOST`
- `UART_RX_HOST`

Use this for the `RP2040` surrogate.

### J4: Native I2C Header

Expose a shared I2C header for the native low-speed peripherals.

Recommended signals:

- `+3V3_AUX`
- `GND`
- `I2C_SDA`
- `I2C_SCL`

Use this for `RTC` and `GNSS` breakouts.

### J5: Compatibility USB Device Connector

This is the connector used for `RTL-SDR` or `Proxmark3` testing.

Acceptable Prototype 0 choices:

- short pigtail to `USB-A` receptacle for dongle-style devices
- `USB-C` receptacle wired as a device-facing convenience port only if you control the target cable path
- pin header for a very short custom USB lead

Practical rule:

- pick the connector that matches the real test device with the least extra cable nonsense

## Cartridge ID and Present Wiring

### ID Strap Block

Provide a simple strap block or DIP switch for:

- `CART_ID0`
- `CART_ID1`

Recommended state model:

- strap to `GND` for logical `0`
- leave to host-side bias for logical `1`

Prototype 0 only needs coarse identity.

### Present Switch

Provide one simple control for `CART_PRESENT_N`.

Recommended model:

- toggle switch or jumper that pulls `CART_PRESENT_N` low when the cartridge is considered inserted

This lets you test detection logic without a physical slot.

## Power Distribution Rules

### `+5V_MAIN`

Use `+5V_MAIN` for:

- compatibility device VBUS where needed
- optional future cartridge-side regulators if testing demands it

Do not assume all native low-speed targets need `5V` directly.

### `+3V3_AUX`

Use `+3V3_AUX` for:

- `RP2040` surrogate logic
- `RTC` breakout
- `GNSS` breakout if the chosen breakout is `3.3V`-safe
- ID and indicator logic if added

## Native Surrogate Wiring

### `RP2040`-Class Controller

Connect:

- host `UART_TX_HOST` -> surrogate RX
- surrogate TX -> host `UART_RX_HOST`
- `+3V3_AUX`
- `GND`

### `RTC`

Connect:

- `I2C_SDA`
- `I2C_SCL`
- `+3V3_AUX`
- `GND`

### `GNSS`

Recommended Prototype 0 approach:

- use `I2C` if the module supports it cleanly and avoids consuming the same UART needed by the RP2040 surrogate
- otherwise document the UART mux compromise explicitly

For Prototype 0, cleaner bus separation is better than realism theater.

## Compatibility Wiring

### `C3-001 RTL-SDR Scout`

Connect through J2/J5 only for data, plus `5V` as needed by the device connector strategy.

Required checks:

- stable VBUS at the device side
- repeatable enumeration
- no visible disconnect under short steady-state use

### `C3-002 Proxmark3 Easy RFID`

Use the same J2/J5 USB path.

Required checks:

- stable VBUS at the device side
- repeatable enumeration or documented failure mode
- current draw and idle stability captured during bring-up

## Suggested Test Points and Indicators

Recommended:

- `TP_5V_CART`
- `TP_3V3_CART`
- `TP_USB_D+`
- `TP_USB_D-`
- `TP_PRESENT_N`
- optional LEDs for `5V`, `3.3V`, and present asserted

## Minimal Wiring Deliverable

The cartridge breakout is sufficiently defined for Prototype 0 when you have:

- J1 and J2 matched to the host breakout headers
- J3 and J4 ready for native surrogate devices
- J5 chosen for the actual compatibility test hardware
- a clear strap and present-control scheme
- test points placed for power and USB sanity checks
