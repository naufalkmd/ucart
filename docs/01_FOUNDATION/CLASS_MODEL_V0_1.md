# Class Model v0.1

## Purpose

Define what `C1`, `C2`, and `C3` actually mean so the project stops collapsing every module into one fake standard.

## Core Distinction

The dividing question is not:

"Was this originally marketed for uConsole?"

The dividing question is:

"Can this module honestly fit the native shell, interface, thermal, and user-experience rules without ugly compromises?"

If yes:

- it belongs in `C1` or `C2`

If no:

- it belongs in `C3`

## Class Definitions

### C1 Native Compact

Use `C1` when the module is:

- designed around the native compact shell
- designed around the native compact faceplate and UX rules
- aligned to the `C1` backplane without compatibility gymnastics
- small and cool enough to fit the compact native envelope honestly

### C2 Native Expanded

Use `C2` when the module is:

- still a native `uCart` design
- too large, hot, or mechanically demanding for `C1`
- better served by a second standardized native envelope

`C2` is a second real standard, not a miscellaneous bin.

### C3 Compatibility

Use `C3` when the module is:

- not a natural native fit
- better handled through an adapter shell, carrier, or compatibility faceplate
- still worth integrating because it meaningfully reduces user friction

`C3` is not “anything third-party.”

`C3` is “non-native fit.”

## Current Mapping

### Native

- `C1-001 Utility Nav`

### Compatibility

- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`

### Deferred

- future native `LoRa/GNSS` cartridges -> likely `C1` or `C2`
- `HackRF One` compatibility study -> likely `C3`

## Design Rule

Do not let `C3` distort `C1`.

Do not let `C1` pretend awkward stock tools are native fits.

Keep both honest.
