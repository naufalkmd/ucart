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

It standardizes the visible user experience of modules by using a cartridge family with a shared shell and insertion behavior.

It does not assume that every module should share the same electrical connector.

## In Scope for v1

- one `uCart Host` attached to uConsole
- one primary cartridge slot
- one shared cartridge shell family for v1
- one primary electrical class: `C1`
- support for stock-tool cartridges using `C1` where practical
- host-side power input and regulation
- repeatable cartridge detection and verification workflow
- serviceable enclosure with exposed status and maintenance access

## Frozen v1 Cartridges

- `C1-001 RTL-SDR Scout`
- `C1-002 Proxmark3 Easy RFID`
- `C1-003 Utility Nav` based on `RP2040 + GNSS + RTC`

## Deferred Candidates

- `HackRF One`
- `LoRa`

## Out of Scope for v1

- one universal connector for every future cartridge
- simultaneous multi-cartridge operation in the primary slot
- forcing `HDMI`, `NVMe`, or `PCIe` modules into the `C1` slot
- full custom host motherboard
- custom SDR redesign
- custom RFID or NFC redesign

## Design Principles

- visual consistency first
- simple insertion and removal workflow first
- stock tools stay stock unless redesign is clearly worth it
- electrical honesty over fake universality
- serviceability beats visual cleanliness
