# C1 Shell Envelope v0.1

## Purpose

Define a provisional outer shell and host slot envelope for the first `C1` cartridge family.

This envelope is intentionally sized around the frozen v1 cartridge set, not around every future module idea.

## Provisional Outer Cartridge Dimensions

Use these as the v0.1 shell target:

- face width: `68 mm`
- body height: `92 mm`
- overall thickness: `18 mm`

Interpretation:

- wide enough for a useful label and front face
- tall enough for `RTL-SDR`-class, `Proxmark3 Easy`-class, and utility internals with carrier adaptation
- still small enough to feel like a deliberate cartridge rather than a full rear-pack slab

## Internal Planning Volume

Plan around this usable body volume after shell walls and retention features:

- internal width target: `60 mm`
- internal height target: `84 mm`
- internal thickness target: `12 mm`

## Front-Face Zone

Reserve the exposed cartridge face for module-specific access:

- antenna connector area
- small status label area
- optional service or breakout cutout

The allowed front-face family variations for `C1` are defined in `C1_FACEPLATE_STRATEGY_V0_1.md`.

## Slot Assumptions

The host slot should assume:

- one consistent insertion direction
- guided rails on both cartridge sides
- a protected connector set back from the slot opening
- positive retention, not loose friction alone

## Why This Size

This size is chosen to favor the first three cartridges:

- `RTL-SDR Scout`
- `Proxmark3 Easy RFID`
- `Utility Nav`

It is not chosen around `HackRF One`.

## Deferred Mechanical Problem

If `HackRF One` becomes a future cartridge, it may require one of these:

- a larger shell family
- a revised internal carrier approach
- a future `C2` form factor

That is a later decision and should not distort `C1` v0.1.
