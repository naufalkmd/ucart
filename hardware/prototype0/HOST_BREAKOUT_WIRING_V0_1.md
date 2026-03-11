# Host Breakout Wiring v0.1

## Purpose

Define the concrete wiring layout for the Prototype 0 host breakout board.

This board is the temporary electrical stand-in for `uCart Host`.

## Board Role

The host breakout board must do four things:

- accept known-good external `5V` input
- provide `+5V_MAIN` and `+3V3_AUX` to the cartridge side
- bridge upstream `USB` host data to the cartridge-side compatibility target
- expose low-speed control and detection signals for probing

## Functional Block Diagram

```text
External 5V input
        |
        +-- fuse / current-limit --> +5V_MAIN switch/jumper --> low-speed harness
        |                                                 \
        |                                                  +-> USB device VBUS to cartridge board
        |
        +-- 3.3V regulator -------------------------------> +3V3_AUX to low-speed harness

Upstream USB host port
        |
        +-- USB_D+ ---------------------------------------> dedicated USB link -> cartridge board
        +-- USB_D- ---------------------------------------> dedicated USB link -> cartridge board
        +-- GND  -----------------------------------------> dedicated USB link -> cartridge board

Host low-speed header / MCU / jumpers
        |
        +-- UART_TX_HOST ---------------------------------> low-speed harness
        +-- UART_RX_HOST <-------------------------------- low-speed harness
        +-- I2C_SDA <------------------------------------> low-speed harness
        +-- I2C_SCL <------------------------------------> low-speed harness
        +-- CART_ID0  <----------------------------------- low-speed harness
        +-- CART_ID1  <----------------------------------- low-speed harness
        +-- CART_PRESENT_N <------------------------------ low-speed harness
```

## Recommended Connectors

### J1: External `5V` Input

Use one simple power connector for the bench supply.

Recommended options:

- `USB-C` receptacle used only as a `5V` input source during bench work
- 2-pin screw terminal if bench supply convenience matters more than cleanliness

Minimum pins:

- `VIN_5V`
- `GND`

### J2: Upstream USB Host Port

This is the host-side data connection to uConsole or a development laptop.

Minimum pins:

- `USB_HOST_D+`
- `USB_HOST_D-`
- `GND`

Practical rule:

- do not source cartridge power from this connector in Prototype 0
- keep it as a data path first
- do not back-feed external `5V` into the upstream host port
- prefer a simple `USB-A` host-facing path or another known-good `USB 2.0` host connection over unnecessary `USB-C` complexity for Prototype 0

### J3: Low-Speed and Power Harness Header

This is the main temporary host-to-cartridge harness.

Recommended size:

- 10 to 12 pins

Recommended signal order:

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

This preserves the frozen logical interface while staying breadboard-friendly.

### J4: Dedicated USB Link Header

This is the short host-to-cartridge `USB 2.0` link.

Recommended signals:

| Pin | Signal |
| --- | ------ |
| 1 | `USB_D-` |
| 2 | `USB_D+` |
| 3 | `GND` |
| 4 | `+5V_MAIN` optional pass-through only if needed by the chosen USB receptacle strategy |

Practical rule:

- if you include `+5V_MAIN` on this header, treat it as convenience only
- the main power path should still be defined on J3

## Required Power Path

### `+5V_MAIN`

Recommended chain:

```text
External 5V input
 -> fuse or current-limit stage
 -> current measurement point
 -> enable jumper or switch
 -> J3 `+5V_MAIN`
 -> optional J4 convenience pass-through
```

Required test points:

- `TP_5V_IN`
- `TP_5V_MAIN`
- `TP_GND`

### `+3V3_AUX`

Recommended chain:

```text
External 5V input
 -> 3.3V regulator
 -> local decoupling
 -> J3 `+3V3_AUX`
```

Required test points:

- `TP_3V3_AUX`
- `TP_GND`

## Low-Speed Signal Wiring

### UART

| Host Signal | J3 Pin | Direction |
| ----------- | ------ | --------- |
| `UART_TX_HOST` | 5 | host -> cartridge |
| `UART_RX_HOST` | 6 | cartridge -> host |

### I2C

| Host Signal | J3 Pin | Direction |
| ----------- | ------ | --------- |
| `I2C_SDA` | 7 | bidirectional |
| `I2C_SCL` | 8 | bidirectional |

Practical rule:

- if pull-ups are present on the host breakout, make them easy to disable
- do not assume the cartridge-side target lacks pull-ups

### Cartridge Detect and ID

| Host Signal | J3 Pin | Direction |
| ----------- | ------ | --------- |
| `CART_ID0` | 9 | cartridge -> host |
| `CART_ID1` | 10 | cartridge -> host |
| `CART_PRESENT_N` | 11 | cartridge -> host |

Recommended host-side biasing:

- weak pull-up on `CART_PRESENT_N`
- weak pull-up or pull-down network on `CART_ID0` and `CART_ID1` that matches the intended strap scheme

## USB Wiring Rules

- keep J2 to J4 as short as practical
- keep `USB_D+` and `USB_D-` together as a pair
- avoid long dupont jumpers for the USB path
- give the USB header a nearby ground reference
- do not share the USB path with switching-current measurements if avoidable

## Minimum Indicators and Controls

Recommended:

- `LED_5V_MAIN`
- `LED_3V3_AUX`
- `JP_5V_EN` or small slide switch for cartridge `5V`
- optional reset button for any local host controller used during testing

## Minimal Wiring Deliverable

The host breakout is sufficiently defined for Prototype 0 when you have:

- connector list for J1 through J4
- exact harness pinout for J3 and J4
- power path with fuse, measurement point, and `5V` enable control
- test point locations for `5V`, `3.3V`, `USB_D+`, `USB_D-`, and `CART_PRESENT_N`
