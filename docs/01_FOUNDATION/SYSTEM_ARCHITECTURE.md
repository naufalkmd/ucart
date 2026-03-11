# System Architecture

## Overview

The system uses uConsole as the host computer and UI while `uCart Host` acts as the cartridge interface.

The core architectural move is:

- one primary host backplane based on the `C1` electrical interface
- native cartridges that are designed around that standard
- compatibility cartridges that bridge external tools onto that host cleanly
- a future expanded native class that does not distort the compact standard

## High-Level Architecture

```text
uConsole Host
|
+- host link to uCart Host
   |
   +- power input and regulation
   |
   +- cartridge detect and control logic
   |
   +- C1 host backplane
   |  +- 5V
   |  +- 3.3V
   |  +- USB 2.0
   |  +- UART
   |  +- I2C
   |  +- ID pins
   |
   +- service and debug access
   |
   +- inserted cartridge
      +- native C1 cartridge
      |    or
      +- C3 compatibility cartridge via carrier/interposer
```

## Class Model

### C1 Native Compact

`C1` is the compact native cartridge standard.

It is for modules that can honestly fit:

- the compact shell assumptions
- the compact thermal and power assumptions
- the consistent native faceplate and UX rules
- the `C1` backplane signal set

Current native example:

- `C1-001 Utility Nav`

Likely future candidates:

- purpose-designed `LoRa`
- purpose-designed `GNSS`
- other native low-power utility modules

### C2 Native Expanded

`C2` is the future expanded native cartridge standard.

It exists for native modules that still belong in the `uCart` ecosystem but need more volume, thermal margin, or a larger shell.

`C2` should stay visually and mechanically consistent as a native class, not a compatibility dumping ground.

### C3 Compatibility

`C3` is the compatibility cartridge class.

It is for devices that do not honestly fit the native standard physically or ergonomically but can still be adapted into the ecosystem.

Current compatibility examples:

- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`

Likely future candidate:

- `C3-003 HackRF One`

## Internal Bus Strategy

- the host backplane remains the `C1` electrical interface in v1
- native `C1` cartridges plug into it directly
- `C3` compatibility cartridges reach it through an internal carrier or interposer as needed
- `USB 2.0` handles USB-native devices
- `UART` handles debug and simple module control paths
- `I2C` handles RTC, sensors, and cartridge ID options

## Power Strategy

- do not assume uConsole alone powers every cartridge reliably
- provide dedicated power input to `uCart Host`
- distribute `5V` for USB-native or adapted compatibility cartridges
- generate `3.3V` for native low-speed logic
- keep noisy power sections away from RF-sensitive cartridge regions

## v1 Success Criteria

- the host can reliably run both a native `C1` cartridge and a `C3` compatibility cartridge
- cartridge insertion and removal feel consistent even when the internals differ by class
- installed cartridge devices enumerate or respond reliably after repeated insertion cycles
- no brownouts or unstable detection during normal use
