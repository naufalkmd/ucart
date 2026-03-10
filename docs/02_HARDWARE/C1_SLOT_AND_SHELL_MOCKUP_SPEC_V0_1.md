# C1 Slot and Shell Mockup Spec v0.1

## Purpose

Define the first concrete geometry targets for a printable `C1` host slot and matching cartridge shell mockup.

This is a prototype-fit specification, not a production-tolerance drawing.

## Scope

This spec is only for the first physical mockup stage.

It is meant to answer these questions:

- does the cartridge feel coherent in the hand
- does the slot guide the cartridge reliably
- is the connector protected well enough
- do the faceplate and shell pieces divide cleanly

## Reference Cartridge Envelope

Use the current `C1` shell envelope as the starting point:

- outer width: `68.0 mm`
- outer height: `92.0 mm`
- outer thickness: `18.0 mm`

Recommended mockup shell wall target:

- general wall thickness: `2.0 mm`

Recommended faceplate thickness:

- faceplate thickness: `2.0 mm`

## Host Slot Opening

Use this as the first printable host slot baseline:

- slot opening width: `69.0 mm`
- slot opening thickness: `19.0 mm`
- visible slot depth before connector zone: `10.0 mm`

Interpretation:

- `0.5 mm` total width clearance over the nominal shell body
- `1.0 mm` total thickness clearance over the nominal shell thickness
- conservative enough for first 3D printed mockups without immediate binding

If the first printed parts are too loose, tighten in small steps after measurement.

## Guide Rail Geometry

Use two internal host rails with matching cartridge body grooves.

### Host Rail Baseline

- rail count: `2`
- rail depth into slot: `1.5 mm`
- rail engagement length: `42.0 mm`
- rail entry chamfer length: `2.0 mm`
- nominal span between rail contact faces: `61.6 mm`

### Cartridge Groove Baseline

- groove depth: `1.8 mm`
- groove height: `3.0 mm`
- nominal span between groove contact faces: `62.0 mm`

Interpretation:

- target running clearance: about `0.2 mm` per side on the guide datum
- enough to slide in a printed mockup without forcing precision machining assumptions

## Connector Setback

Use this as the first protected connector baseline:

- card-edge socket mouth setback from slot opening: `10.0 mm`
- first electrical contact should not occur before roughly `8.0 mm` of insertion travel
- cartridge should still have guided support before the edge fingers reach the socket

Design rule:

- the connector must not be the first thing that aligns the cartridge
- rails and shell geometry must do that job first

## End-Stop and Travel

Use this initial mockup rule:

- shell hard end-stop should define final seated position
- connector mating should happen near the end of travel, not across the full travel
- leave `1.0 mm` to `2.0 mm` of shell-controlled overtravel margin after first solid connector engagement, depending on connector choice

This keeps insertion force reacting into the shell instead of directly into the connector.

## Latch Location

Use one simple latch position for the first mockup.

### Recommended Baseline

- latch type: single spring latch or printed detent for mockup
- latch location: centered on the rear host wall
- latch engagement notch centerline: `8.0 mm` below the cartridge top edge
- latch notch width: `10.0 mm`
- latch notch depth: `1.5 mm`

Interpretation:

- one central latch is enough to prove the interaction model
- production retention can change later, but the mockup should prove where the lock event happens

## Faceplate Mounting Pattern

Use a simple four-point mount pattern for the first shell mockup.

### Baseline Pattern

- mount count: `4`
- fastener size target: `M2` prototype screws or equivalent printed bosses
- horizontal pitch: `56.0 mm`
- vertical pitch: `76.0 mm`
- side inset from outer edge: `6.0 mm`
- top and bottom inset from outer edge: `8.0 mm`

Interpretation:

- stable enough for repeated faceplate swaps during prototype work
- easy to adapt later into clips, heat-set inserts, or hidden fasteners if desired

## Internal Carrier Datum

Use one fixed carrier reference so cartridges do not redefine connector alignment.

### Baseline

- carrier PCB thickness target: `1.6 mm`
- carrier connector edge reference remains fixed relative to the shell top edge
- carrier mounting plane should sit centrally in the shell body volume
- cartridges adapt their internals to the carrier, not the other way around

## Mockup Material Assumptions

For the first physical mockup:

- printed shell and host parts are acceptable
- do not assume production shrink or injection-molding tolerances yet
- adjust only after measuring the first printed sample set

## What To Measure First

After printing the first mockup, check these in order:

1. cartridge slides without binding
2. latch engages consistently
3. connector stays protected during insertion
4. faceplate swap does not affect shell alignment
5. cartridge does not wobble excessively when seated

## Expected Revision Points

The most likely values to change after the first mockup are:

- rail clearance
- slot opening thickness
- latch notch depth
- connector setback by a few millimeters

The least likely values to change should be:

- overall cartridge envelope
- basic top-loading direction
- shared shell plus faceplate model
