# v1 Slot-Compatible Shell Envelope v0.1

## Purpose

Define the provisional outer shell and host slot envelope for the first slot-compatible cartridge body used in `uCart` v1.

## Decision Summary

For `v1`, the current shell body is shared by:

- native `C1` compact cartridges that honestly fit the compact standard
- the first small `C3` compatibility cartridges that can be adapted without forcing a bigger body

This does not mean `C1` and `C3` are the same class.

It means they share the same first host-fit outer body in `v1`.

## Why This Is the Right v1 Decision

- one host slot is easier to prototype honestly
- one body keeps the first physical mockup effort focused
- native `C1` stays protected by class rules, not by pretending it needs a different shell on day one
- early `C3` compatibility cartridges can exist without polluting the native backplane definition

## Provisional Outer Cartridge Dimensions

Use these as the `v1` shell target:

- face width: `68 mm`
- body height: `92 mm`
- overall thickness: `18 mm`

Interpretation:

- wide enough for a useful label and front face
- tall enough for `Utility Nav`, `RTL-SDR Scout`, and `Proxmark3 Easy RFID` with carrier adaptation
- still small enough to feel like a deliberate cartridge rather than a rear-pack slab

## Internal Planning Volume

Plan around this usable body volume after shell walls and retention features:

- internal width target: `60 mm`
- internal height target: `84 mm`
- internal thickness target: `12 mm`

How this volume is divided between the shared body, faceplate, and internal carrier is defined in `V1_SLOT_COMPATIBLE_SHELL_BREAKDOWN_V0_1.md`.

## Front-Face Zone

Reserve the exposed cartridge face for module-specific access:

- antenna connector area
- small status label area
- optional service or breakout cutout

Native and compatibility faceplate rules are defined in `V1_FACEPLATE_STRATEGY_V0_1.md`.

## Slot Assumptions

The host slot should assume:

- one consistent insertion direction
- guided rails on both cartridge sides
- a protected connector set back from the slot opening
- positive retention, not loose friction alone

## Why This Size

This size is chosen to favor the frozen `v1` set:

- `C1-001 Utility Nav`
- `C3-001 RTL-SDR Scout`
- `C3-002 Proxmark3 Easy RFID`

It is not chosen around `HackRF One`.

## Deferred Mechanical Problem

If a future cartridge does not fit this shared `v1` body honestly, it should trigger one of these:

- a future native `C2` body
- a larger `C3` compatibility body
- a revised shell family after physical evidence, not before

`HackRF One` is the obvious future study candidate here.
