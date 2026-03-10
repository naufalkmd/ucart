# Cartridge Standard v0.1

## Purpose

Define a realistic v1 cartridge standard that creates visual consistency and lower friction without pretending every module shares the same electrical needs.

## Core Rule

Standardize the cartridge experience first.

Do not require every future cartridge to use the same electrical class.

## Standardized Elements

### Visual and Mechanical Standard

Cartridges should align around the same physical rules where practical:

- common outer shell family
- common insertion direction
- common latch or retention style
- common front-face width and label zone
- common orientation markers
- common user expectation for install and removal

### Service Standard

Every supported v1 cartridge should be:

- insertable without opening the entire host
- removable without rewiring the system
- identifiable by label and cartridge ID
- accessible for antenna or service cable attachment on the cartridge face

## Electrical Classes

### C1 Standard Cartridge

#### Intended Use

USB-native tools and low-complexity utility cartridges.

#### Required Support

- `5V`
- `3.3V`
- `GND`
- `USB 2.0 D+ / D-`
- `UART TX / RX`
- `I2C SDA / SCL`
- ID pins or small ID device

#### Typical Examples

- `HackRF`
- `RTL-SDR`
- `Proxmark3`
- many `LoRa` boards
- `GNSS`
- `RTC`
- `RP2040` utility boards

### C2 Exception Cartridge

#### Intended Use

Future cartridges that need a visually compatible shell but cannot fit the `C1` electrical assumptions.

#### Typical Examples

- `HDMI` plus `USB` KVM devices
- `NVMe` or `PCIe` based concepts

#### Rule

`C2` is not part of v1 and must not complicate the `C1` slot.

## What Is Not Standardized in v0.1

- one universal blind-mate connector for every future cartridge
- `HDMI`, `NVMe`, or `PCIe` inside `C1`
- one internal PCB shape for all cartridges
- simultaneous support for multiple active cartridges in the primary slot

## Frozen v1 Cartridge Set

- `C1-001 RTL-SDR Scout`
- `C1-002 Proxmark3 Easy RFID`
- `C1-003 Utility Nav` based on `RP2040 + GNSS + RTC`

Deferred from the frozen set:

- `HackRF One`
- `LoRa`

## Exit Criteria for v0.1

- `C1` signal set is frozen
- first three cartridges are selected
- outer shell and slot geometry are selected
- retention and insertion concept is selected
- host power and detection assumptions are documented
