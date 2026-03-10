# uCart

A cartridge-based expansion project for uConsole focused on reducing the friction of using different modules.

## Goal

Build a visually consistent cartridge system for uConsole that makes modules faster to insert, power, detect, and use.

The product goal is not one universal electrical connector for everything. The product goal is one clean cartridge experience.

## v1 Direction

- uConsole remains the host compute and UI platform
- `uCart Host` provides the female slot, power, and detection logic
- cartridges share one visual shell and insertion behavior where practical
- one cartridge is active in the primary slot at a time
- `C1` is the primary cartridge electrical class for v1
- stock tools stay stock whenever possible and are adapted inside cartridges

## Cartridge Classes

- `C1 Standard Cartridge`: `USB 2.0`, `5V`, `3.3V`, `UART`, `I2C`, and ID pins
- `C2 Exception Cartridge`: future visually compatible class for modules that cannot fit `C1`

## Frozen v1 Cartridges

- `C1-001 RTL-SDR Scout`
- `C1-002 Proxmark3 Easy RFID`
- `C1-003 Utility Nav` built around `RP2040 + GNSS + RTC`

Deferred from the frozen v1 set:

- `HackRF One`
- `LoRa`

## Planned v1 Support

- `C1` cartridge support for the frozen v1 set above
- host-side power input, device detection, and simple service access

## Repository Layout

- `docs/` project docs and architecture
- `hardware/` cartridge shell, slot, and interface assets
- `software/` host-side setup, scripts, and detection logic

## First Milestone

1. freeze `Cartridge Standard v0.1`
2. choose the first three supported cartridges
3. prove insertion, detection, and power stability on a simple prototype
