# System Architecture

## Overview

The system uses uConsole as the host computer and UI while `uCart Host` acts as the female cartridge interface.

The core architectural move is:

- one shared cartridge shell family
- one primary slot for one cartridge at a time
- one realistic `C1` electrical class for v1
- future exception classes only if they are justified later

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
   +- C1 cartridge backplane
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
      +- stock tool or custom board
      +- internal carrier or adapter
      +- module-specific ports and antenna exits
```

## Cartridge Strategy

### Shared Visual Standard

Cartridges should feel like one product family:

- same outer silhouette where practical
- same insertion direction
- same latch or retention behavior
- same visible front-face language
- same labeling zone and orientation markers

### C1 Standard Cartridge

`C1` is the only cartridge electrical class in v1.

It is designed for devices that can reasonably live behind:

- `5V`
- `3.3V`
- `USB 2.0`
- `UART`
- `I2C`
- ID pins

Likely fits:

- `HackRF`
- `RTL-SDR`
- `Proxmark3`
- many `LoRa` boards
- `GNSS`
- `RTC`
- `RP2040` utility designs

### Future Exception Classes

If a future module needs `HDMI`, `NVMe`, or `PCIe`, it should not distort `C1`.

Those cases belong in a separate future class or a separate attachment path.

## Internal Bus Strategy

- `USB 2.0` handles stock-tool cartridges and USB-native devices
- `UART` handles debug and some module control paths
- `I2C` handles RTC, low-speed sensors, and cartridge ID options
- optional GPIO sideband is limited to local control and status

## Power Strategy

- do not assume uConsole alone powers every cartridge reliably
- provide dedicated power input to `uCart Host`
- distribute `5V` for USB-native cartridges
- generate `3.3V` for low-speed logic
- keep noisy power sections away from RF-sensitive cartridge regions

## v1 Success Criteria

- cartridge insertion and removal feels consistent across the first three cartridges
- the host can reliably answer which cartridge is inserted
- installed cartridge devices enumerate or respond reliably after repeated insertion cycles
- no brownouts or unstable detection during normal use
