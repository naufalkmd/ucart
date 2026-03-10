# C1 Faceplate Strategy v0.1

## Purpose

Define how much of the `C1` cartridge shell is shared across modules and where faceplate variation is allowed.

This exists to stop the project from drifting into one fully custom shell per cartridge.

## Core Rule

`C1` uses one shared shell family.

It does not use one totally different full shell per module.

What changes by module should be as limited as possible.

The shell-part breakdown behind this rule is defined in `C1_SHELL_BREAKDOWN_V0_1.md`.

## Shared Across All C1 Cartridges

These should stay common across the full `C1` family:

- outer shell envelope
- insertion direction
- latch and retention features
- rail geometry
- connector position relative to the shell
- main label zone
- overall visual language

## Allowed To Vary By Cartridge

These can vary where needed:

- internal carrier or bracket
- front faceplate geometry
- antenna opening
- small service cutouts
- LED window or button opening
- internal adapter PCB

## Faceplate Families

For `C1 v0.1`, standardize only `3` faceplate families.

### 1. RF Faceplate

#### Intended Use

Cartridges that mainly need one RF connector and minimal user interaction.

#### Typical Features

- one standard RF connector cutout area
- optional small LED opening
- simple printed label zone

#### Candidate Cartridges

- `C1-001 RTL-SDR Scout`
- many future `LoRa` cartridges
- some future `GNSS` cartridges with external antenna connector
- possible future `HackRF` study, but not guaranteed

### 2. RFID Faceplate

#### Intended Use

Cartridges that need a usable tap or interaction zone rather than a simple connector-first face.

#### Typical Features

- non-metal interaction window or reduced-obstruction front area
- optional small LED opening
- minimal clutter on the active face

#### Candidate Cartridges

- `C1-002 Proxmark3 Easy RFID`

#### Why It Is Separate

`Proxmark3` is the obvious faceplate outlier in `C1` because user interaction happens against the face itself.

### 3. Utility Faceplate

#### Intended Use

Cartridges that expose low-speed utility behavior, status, or simple service access.

#### Typical Features

- small status LED opening
- optional small button opening
- optional IR window or debug opening
- optional minimal port or header cutout

#### Candidate Cartridges

- `C1-003 Utility Nav`
- future `RP2040` utility cartridges
- simple `GNSS/RTC` utility variants
- simple debug or sensor cartridges

## Minimal Faceplate Rule

If a cartridge can fit one of the existing faceplate families with only a cutout change, do not create a new family.

A new faceplate family is only justified when:

- user interaction model is materially different
- RF or sensing performance needs a different front-face material or geometry
- the cartridge becomes awkward or misleading with the existing family shapes

## Current Cartridge Mapping

| Cartridge ID         | Cartridge Name         | Faceplate Family |
| -------------------- | ---------------------- | ---------------- |
| `C1-001`             | `RTL-SDR Scout`        | `RF`             |
| `C1-002`             | `Proxmark3 Easy RFID`  | `RFID`           |
| `C1-003`             | `Utility Nav`          | `Utility`        |
| future `LoRa`        | `TBD`                  | `RF` or `Utility` depending on board behavior |
| future `GNSS` only   | `TBD`                  | `RF` or `Utility` depending on antenna strategy |
| future `HackRF One`  | `TBD`                  | likely not decided by faceplate alone |

## Important Warning

`HackRF One` is not just a faceplate problem.

It may become a larger shell, a revised internal carrier, or even a future `C2` problem depending on thermal and volume constraints.

Do not let `HackRF One` distort the `C1` faceplate system.

## Exit Criteria

This strategy is complete when:

- the three `C1` faceplate families are accepted as the only v0.1 families
- each frozen v1 cartridge is mapped to one family
- shell work begins from a shared shell plus swappable faceplate model
