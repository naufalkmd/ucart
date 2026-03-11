# Prototype 0 KiCad Schematic Checklist v0.1

## Purpose

Define the minimum KiCad schematic work needed to turn Prototype 0 from a document set into an electrical design package.

This is a schematic-capture checklist, not a PCB-layout plan.

## Goal

Before buying parts, the KiCad work should answer these questions:

- is the host breakout electrically coherent
- is the cartridge breakout electrically coherent
- are power, detect, and low-speed nets named consistently
- is the temporary harness split clear enough to build without improvising

## Scope

Prototype 0 KiCad work should include:

- one host breakout schematic
- one cartridge breakout schematic
- explicit harness connectors between them
- named test points
- placeholder parts where exact sourcing is still open

Prototype 0 KiCad work does not need:

- final slot connector symbols or footprints
- production mechanical constraints
- final cartridge carrier layout
- `HackRF` or future `C2` support

## Project Structure

Recommended structure:

- `host_breakout.kicad_sch`
- `cartridge_breakout.kicad_sch`
- optional shared symbol sheet for the temporary harness pinout

If you prefer one KiCad project with hierarchical sheets, use:

- top sheet for Prototype 0
- one host breakout sheet
- one cartridge breakout sheet

## Host Breakout Checklist

### Power Input

Include:

- external `5V` input connector
- fuse or current-limit stage on `+5V_MAIN`
- current measurement point or current-sense placeholder
- `+5V_MAIN` enable jumper or switch
- `3.3V` regulator for `+3V3_AUX`
- input and output decoupling around the regulator

Required net names:

- `VIN_5V`
- `+5V_MAIN`
- `+3V3_AUX`
- `GND`

### Upstream USB Host Path

Include:

- upstream host USB connector
- direct data path for `USB_D+` and `USB_D-`
- clear ground reference
- no back-feed path from external `5V` into the upstream USB host connector

Required net names:

- `USB_HOST_D+`
- `USB_HOST_D-`
- `USB_D+`
- `USB_D-`

Practical rule:

- if you are unsure how to make a safe host-facing `USB-C` input path, use a simpler `USB 2.0` host connector for Prototype 0

### Low-Speed and Detect Nets

Include:

- `UART_TX_HOST`
- `UART_RX_HOST`
- `I2C_SDA`
- `I2C_SCL`
- `CART_ID0`
- `CART_ID1`
- `CART_PRESENT_N`

Add host-side biasing where intended:

- weak pull-up on `CART_PRESENT_N`
- defined bias scheme for `CART_ID0` and `CART_ID1`
- optional pull-up footprint control for `I2C`

### Host Connectors and Test Points

Include:

- low-speed and power harness connector
- dedicated USB harness connector
- test points for `+5V_MAIN`, `+3V3_AUX`, `USB_D+`, `USB_D-`, `CART_PRESENT_N`, and `GND`
- optional indicator LEDs for `5V` and `3.3V`

## Cartridge Breakout Checklist

### Harness Inputs

Include:

- low-speed and power harness connector with the frozen J3 pinout
- dedicated USB harness connector with the frozen J4 pinout

Required net names must match the host side exactly.

### Native Surrogate Headers

Include:

- native UART header for the `RP2040` surrogate
- native `I2C` header for `RTC` and `GNSS` surrogate devices
- optional breakout header for extra `3.3V` and `GND`

### Cartridge Detect and ID Controls

Include:

- strap or DIP-switch network for `CART_ID0`
- strap or DIP-switch network for `CART_ID1`
- present switch or jumper for `CART_PRESENT_N`

Practical rule:

- make the logic states readable without needing to inspect the schematic every time

### Compatibility USB Path

Include:

- one device-side USB connector or pigtail header for `RTL-SDR` and `Proxmark3`
- direct short data path from the USB harness to the compatibility-device connector
- optional `+5V_MAIN` convenience pass-through only if the chosen connector strategy actually needs it

### Cartridge Test Points

Include:

- `TP_5V_CART`
- `TP_3V3_CART`
- `TP_USB_D+`
- `TP_USB_D-`
- `TP_PRESENT_N`
- `GND`

## Harness Definition Checklist

Represent the temporary harnesses explicitly in KiCad.

Do not leave them as implied text notes.

### Low-Speed and Power Harness

Must carry:

- `+5V_MAIN`
- `+3V3_AUX`
- `GND`
- `UART_TX_HOST`
- `UART_RX_HOST`
- `I2C_SDA`
- `I2C_SCL`
- `CART_ID0`
- `CART_ID1`
- `CART_PRESENT_N`
- extra `GND`

### Dedicated USB Harness

Must carry:

- `USB_D+`
- `USB_D-`
- `GND`
- optional `+5V_MAIN` only if required by the chosen connector strategy

## Placeholder Part Policy

It is acceptable to use placeholder symbols and footprints for:

- fuse or current-limited power switch
- regulator
- temporary harness connectors
- device-side USB connector

But the schematic should still show:

- electrical role
- direction of power flow
- no-backfeed intent
- expected pin count

## ERC and Review Checklist

Before calling the schematic usable:

- run ERC on both host and cartridge sheets
- confirm identical harness pin numbering on both ends
- confirm the `C1` logical net names match the interface spec exactly
- confirm no direct external `5V` back-feed path to the upstream USB host connector
- confirm all test points needed by the Prototype 0 plan exist in the schematic
- confirm the cartridge ID and present nets have defined logic states

## Deliverables

The KiCad stage is good enough for Prototype 0 when you have:

- host breakout schematic PDF
- cartridge breakout schematic PDF
- exported harness pinout reference
- short review note listing open placeholder parts

## Exit Condition

This checklist is complete when the KiCad design is clean enough that buying parts becomes a sourcing problem, not an architecture problem.
