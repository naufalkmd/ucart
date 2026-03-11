# Prototype 0 Harness Pinout v0.1

## Purpose

Freeze the temporary host-to-cartridge wiring between the Prototype 0 host breakout and cartridge breakout.

This is not the future slot connector.

## Harness Split

Prototype 0 uses two separate harnesses:

- one low-speed and power harness
- one short dedicated USB harness

## J3 Low-Speed and Power Harness

| Pin | Signal | Notes |
| --- | ------ | ----- |
| 1 | `+5V_MAIN` | cartridge main power |
| 2 | `+5V_MAIN` | duplicated for current margin |
| 3 | `GND` | return |
| 4 | `+3V3_AUX` | low-speed logic rail |
| 5 | `UART_TX_HOST` | host -> cartridge |
| 6 | `UART_RX_HOST` | cartridge -> host |
| 7 | `I2C_SDA` | bidirectional |
| 8 | `I2C_SCL` | bidirectional |
| 9 | `CART_ID0` | cartridge strap to host |
| 10 | `CART_ID1` | cartridge strap to host |
| 11 | `CART_PRESENT_N` | asserted low when inserted |
| 12 | `GND` | return |

## J4 Dedicated USB Harness

| Pin | Signal | Notes |
| --- | ------ | ----- |
| 1 | `USB_D-` | short dedicated path |
| 2 | `USB_D+` | short dedicated path |
| 3 | `GND` | local reference |
| 4 | optional `+5V_MAIN` | only if the chosen USB connector strategy needs it |

## Practical Rules

- keep the USB harness shorter than the low-speed harness if possible
- avoid random dupont wire for `USB_D+` and `USB_D-`
- keep the pin numbering identical on the host and cartridge boards
- do not let this temporary harness layout drift into the production slot definition by accident
