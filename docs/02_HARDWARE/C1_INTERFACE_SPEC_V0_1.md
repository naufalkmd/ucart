# C1 Interface Spec v0.1

## Purpose

Define the first logical signal set for the `C1` host backplane.

This document freezes the primary host-side signal model for v0.1.

Native `C1` cartridges plug into this interface directly.

`C3` compatibility cartridges may reach it through an internal carrier or interposer.

The recommended slot and connector direction is documented in `C1_CONNECTOR_AND_SLOT_V0_1.md`.

The first electrical proof build is documented in `PROTOTYPE_0_BREAKOUT_SPEC_V0_1.md`.

The exact production connector part is still open.

## Design Intent

The `C1` host backplane should support:

- USB-native cartridges
- low-speed utility cartridges
- simple cartridge identification

`C1` should not try to support `HDMI`, `NVMe`, or `PCIe`.

## Logical Signal Set

| Pin | Signal         | Direction        | Notes |
| --- | -------------- | ---------------- | ----- |
| 1   | GND            | shared           | ground return |
| 2   | +5V_MAIN       | host -> cart     | primary cartridge power |
| 3   | +5V_MAIN       | host -> cart     | duplicated for current margin |
| 4   | GND            | shared           | ground return |
| 5   | USB_D-         | bidirectional    | USB 2.0 differential pair |
| 6   | USB_D+         | bidirectional    | USB 2.0 differential pair |
| 7   | GND            | shared           | pair reference |
| 8   | +3V3_AUX       | host -> cart     | low-speed logic rail |
| 9   | UART_TX_HOST   | host -> cart     | host transmit |
| 10  | UART_RX_HOST   | cart -> host     | host receive |
| 11  | I2C_SDA        | bidirectional    | open-drain |
| 12  | I2C_SCL        | host <-> cart    | open-drain |
| 13  | CART_ID0       | cart -> host     | strap or ID device support |
| 14  | CART_ID1       | cart -> host     | strap or ID device support |
| 15  | CART_PRESENT_N | cart -> host     | asserted low when inserted |
| 16  | GND            | shared           | ground return |

## Power Assumptions

### `+5V_MAIN`

- target: `5V`
- budget: `1.5A` continuous per cartridge for v0.1 planning
- peak planning headroom: `2.0A`

### `+3V3_AUX`

- target: `3.3V`
- budget: `300mA` continuous for low-speed logic and light utility loads

## USB Rules

- `C1` is `USB 2.0` only in v0.1
- keep the differential pair short and direct inside host and cartridge
- do not promise hot-swap reliability until the first host prototype proves it

## ID Strategy

v0.1 allows two simple approaches:

- passive strap on `CART_ID0` and `CART_ID1`
- small ID device reachable over `I2C`

Recommended v0.1 rule:

- use strap-based coarse cartridge class ID first
- add richer ID later only if needed

## Recommended v0.1 Connector Behavior

- ground should mate before signal where possible
- the connector should be mechanically protected inside the host slot
- insertion should not expose the user directly to signal contacts

## Explicit Non-Goals

- `USB 3.x`
- `HDMI`
- `PCIe`
- universal future-proofing
