# Project Scope

## Problem Statement

Using several uConsole extensions and external tools creates too much friction:

- too many cables
- inconsistent mounting
- inconsistent power paths
- poor serviceability
- unpredictable setup and device detection

## Project Definition

`uCart` is a cartridge-based expansion system for uConsole.

It standardizes the visible user experience of modules by splitting them into:

- native cartridges that are designed around the standard from day one
- compatibility cartridges that adapt external tools without pretending they are native fits

## In Scope for v1

- one `uCart Host` attached to uConsole
- one primary host slot using the `C1` electrical backplane
- `C1` native compact cartridge definition
- `C2` high-level native expanded cartridge definition
- `C3` compatibility cartridge definition
- one frozen native `C1` cartridge
- two frozen `C3` compatibility cartridges
- host-side power input and regulation
- repeatable cartridge detection and verification workflow
- serviceable enclosure with exposed status and maintenance access

## Frozen v1 Cartridges

- `C1-001 Utility Nav` based on `RP2040 + GNSS + RTC`
- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`

## Deferred Candidates

- future native `LoRa/GNSS` cartridge candidates for `C1` or `C2`
- `C3-003 HackRF One` compatibility study

## Out of Scope for v1

- one universal connector for every future cartridge
- simultaneous multi-cartridge operation in the primary slot
- forcing `HackRF` or `Proxmark3` to pretend they are native `C1` fits
- forcing `HDMI`, `NVMe`, or `PCIe` modules into the primary `C1` slot
- full custom host motherboard

## Design Principles

- visual consistency first
- native standards stay honest
- compatibility cartridges are allowed when they reduce user friction without polluting the native standard
- serviceability beats visual cleanliness
- electrical honesty over fake universality
