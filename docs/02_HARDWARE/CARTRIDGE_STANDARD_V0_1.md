# Cartridge Standard v0.1

## Purpose

Define the first real cartridge class model for `uCart`.

The project needs native standards and a compatibility class.

It should not pretend those are the same thing.

## Core Rule

Standardize the native cartridge experience honestly.

Use compatibility cartridges when they reduce friction without polluting the native standards.

## Standardized Elements

### Shared Ecosystem Rules

Across the ecosystem, standardize where practical:

- cartridge insertion direction
- host-side slot behavior
- labeling language
- detection workflow
- visual family identity

### Native vs Compatibility Rule

- `C1` and `C2` are real native standards
- `C3` is a compatibility class

## Class Definitions

### C1 Native Compact

#### Intended Use

Compact native cartridges that are designed around the standard from day one.

#### Required Support

- direct use of the `C1` host backplane
- compact native shell assumptions
- consistent native compact faceplate and UX rules

#### Example

- `C1-001 Utility Nav`

### C2 Native Expanded

#### Intended Use

Larger native cartridges that still belong in the standard ecosystem but need a second native envelope.

#### Rule

`C2` is a second standard, not a dumping ground.

`C2` is not frozen in v1.

### C3 Compatibility

#### Intended Use

Compatibility cartridges for stock external tools that do not honestly fit the native standard.

#### Required Support

- host integration through the `C1` backplane where practical
- adapter carrier or interposer as needed
- compatibility shell and faceplate rules instead of pretending to be native

#### Examples

- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`
- future `C3-003 HackRF One` study

## What Is Not Standardized in v0.1

- one universal cartridge for every future module
- forcing awkward stock tools into `C1`
- forcing `HDMI`, `NVMe`, or `PCIe` modules into the primary host slot
- one internal PCB shape for all cartridges

## Frozen v1 Cartridge Set

- `C1-001 Utility Nav`
- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`

Deferred from the frozen set:

- future native `LoRa/GNSS` candidates for `C1` or `C2`
- `C3-003 HackRF One` study

## Exit Criteria for v0.1

- the `C1/C2/C3` class model is frozen
- the `C1` host backplane signal set is frozen
- the first native and compatibility cartridges are selected
- shell and faceplate rules are documented for both native and compatibility paths
