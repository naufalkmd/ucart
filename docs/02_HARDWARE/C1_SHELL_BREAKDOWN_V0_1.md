# C1 Shell Breakdown v0.1

## Purpose

Define the actual shell-part strategy for `C1` so the project uses one shell family with limited variation instead of drifting into one-off cartridge enclosures.

## Core Rule

A `C1` cartridge is made from a small number of repeatable parts:

- one shared main shell body
- one swappable front faceplate
- one cartridge-specific internal carrier or bracket set

Optional minor parts are allowed, but the system should not require a fully different outer shell for each cartridge.

## Shared Shell Architecture

### 1. Main Shell Body

This is the common structural body used across the `C1` family.

It should define:

- overall outer dimensions
- rail contact surfaces
- latch and retention features
- connector position reference
- main label plane
- internal mounting datum for the carrier

This part should stay the same across the frozen `C1` v1 cartridges unless physical prototype results force a shell revision.

### 2. Swappable Front Faceplate

This is the visible module-specific front piece.

It should define:

- connector or antenna opening geometry
- non-metal or reduced-obstruction interaction window where needed
- LED or button openings
- family-specific visual identity within the shared shell language

For `C1 v0.1`, this should be limited to the three accepted faceplate families:

- `RF`
- `RFID`
- `Utility`

### 3. Internal Carrier or Bracket Set

This is the cartridge-specific internal adaptation layer.

It should define:

- how the actual board is mounted inside the shell
- how the board reaches the carrier edge connector or interposer
- how local standoffs, spacers, or shields are placed
- how antenna pigtails or small internal cables are restrained

This is the part that should vary the most between cartridges.

### 4. Small Secondary Parts

Allowed when necessary:

- light pipe or LED diffuser
- button plunger
- antenna strain relief piece
- local insulating insert
- RFID interaction window insert

These should remain small support parts, not a hidden second shell system.

## Recommended Part Breakdown for v0.1

Minimum practical cartridge stack:

1. main shell body
2. faceplate piece
3. internal carrier or bracket set
4. fasteners or clips only if required by the shell design

If a cartridge design needs more than this plus a few small support parts, the design should be challenged before it is accepted.

## Internal Mounting Zones

### Connector Zone

Located near the cartridge edge that mates with the host.

Rules:

- keep the carrier connector reference fixed across all cartridges
- do not let free-floating wires define connector alignment
- keep stiff mechanical support near the edge-finger region or interposer zone

### Main Volume Zone

Located in the center of the shell body.

Rules:

- this is where stock boards or utility PCBs sit on the internal carrier
- module-specific brackets should adapt the board to this zone, not redefine the whole shell

### Face Zone

Located behind the swappable faceplate.

Rules:

- reserve this zone for connector cutouts, interaction windows, and LEDs
- avoid using the faceplate as the primary structural mount for the whole module

### Retention Zone

Located near the latch or top stop geometry.

Rules:

- retention loads should be reacted into the shell body, not fragile internal PCBs
- faceplate swap should not compromise slot retention features

## Frozen v1 Cartridge Mapping

| Cartridge ID | Cartridge Name        | Shared Main Shell | Faceplate | Internal Carrier |
| ------------ | --------------------- | ----------------- | --------- | ---------------- |
| `C1-001`     | `RTL-SDR Scout`       | Yes               | `RF`      | custom RTL-SDR carrier |
| `C1-002`     | `Proxmark3 Easy RFID` | Yes               | `RFID`    | custom Proxmark carrier |
| `C1-003`     | `Utility Nav`         | Yes               | `Utility` | utility PCB carrier |

## What Should Not Vary in v0.1

Do not vary these per cartridge unless testing proves the baseline is wrong:

- full outer shell silhouette
- slot rail geometry
- connector depth reference
- latch concept
- gross body thickness

## What May Force a Future Shell Split

These are real reasons to create a future shell family or `C2` body, not just a new faceplate:

- significantly larger board volume
- materially higher thermal load
- multiple RF connector exits that cannot fit the shared face zone cleanly
- structural conflict with the current latch and rail geometry

`HackRF One` is the obvious future candidate that may hit one or more of these limits.

## Practical Design Rule

If a new cartridge can be solved by changing only:

- the faceplate
- the internal carrier
- minor support parts

then it still belongs in the `C1` shell family.

If it needs a new outer body, challenge it hard before accepting that change.
