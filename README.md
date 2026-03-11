# uCart

A cartridge-based expansion project for uConsole focused on reducing the friction of using different modules.

## Goal

Build a visually consistent cartridge ecosystem for uConsole that makes modules faster to insert, power, detect, and use.

The product goal is not one universal cartridge for everything. The product goal is a clean split between native standards and compatibility cartridges.

## v1 Direction

- uConsole remains the host compute and UI platform
- `uCart Host` provides one primary slot, power, and detection logic
- `C1` is the compact native cartridge standard
- `C2` is the future expanded native cartridge standard
- `C3` is the compatibility cartridge class for devices that do not honestly fit the native shell and UX rules
- the primary host backplane remains the `C1` electrical interface in v1

## Cartridge Classes

- `C1 Native Compact`: standard native cartridge with consistent shell and faceplate behavior
- `C2 Native Expanded`: larger native cartridge class, same ecosystem, not yet frozen
- `C3 Compatibility`: adapter-style cartridge for stock external tools using the host interface where practical

## Frozen v1 Cartridges

- `C1-001 Utility Nav` built around `RP2040 + GNSS + RTC`
- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`

Deferred from the frozen v1 set:

- future native `LoRa/GNSS` cartridge candidates for `C1` or `C2`
- `C3-003 HackRF One` compatibility study

## Planned v1 Support

- one native `C1` cartridge proving the standard is real
- two `C3` compatibility cartridges proving stock tools can be adapted cleanly
- host-side power input, device detection, and simple service access

## Repository Layout

- `docs/` project docs and architecture
- `hardware/` cartridge shell, slot, and interface assets
- `software/` host-side setup, scripts, and detection logic

## First Milestone

1. freeze the `C1/C2/C3` class model
2. prove one native cartridge and one compatibility cartridge in the same host
3. validate insertion, detection, and power stability on a simple prototype
