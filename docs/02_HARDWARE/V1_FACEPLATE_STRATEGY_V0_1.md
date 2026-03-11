# v1 Faceplate Strategy v0.1

## Purpose

Define how faceplate consistency works across native and compatibility cartridges.

This exists to prevent two failure modes:

- native cartridges becoming visually inconsistent
- compatibility cartridges pretending they should follow native face rules when they clearly should not

## Core Rule

- `C1` uses one native compact faceplate family
- `C2` will use one native expanded faceplate family when it is defined
- `C3` may use multiple compatibility faceplate families

## Native Faceplate Rules

### C1 Native Compact Faceplate

`C1` should have one consistent face language.

It should define:

- one stable front-face layout philosophy
- one stable label zone
- one stable indicator or small-service pattern where practical

Current native mapping:

- `C1-001 Utility Nav`

### C2 Native Expanded Faceplate

Reserved for the future expanded native class.

Do not define it in detail before `C2` exists.

## Compatibility Faceplate Families

### C3 RF

For compatibility cartridges that mainly need RF connector access and simple labels.

Current mapping:

- `C3-001 RTL-SDR Scout`
- future RF-oriented compatibility cartridges where appropriate

### C3 RFID

For compatibility cartridges where user interaction happens against the face.

Current mapping:

- `C3-002 Proxmark3 Easy RFID`

### C3 Utility-Compatible

Reserved only if a future non-native utility board actually needs a compatibility face.

Do not create it just to mirror native `C1`.

## Mapping Table

| Cartridge ID | Cartridge Name        | Faceplate Strategy |
| ------------ | --------------------- | ------------------ |
| `C1-001`     | `Utility Nav`         | native compact     |
| `C3-001`     | `RTL-SDR Scout`       | `C3 RF`            |
| `C3-002`     | `Proxmark3 Easy RFID` | `C3 RFID`          |
| future native `LoRa/GNSS` | `TBD`      | native compact or native expanded |
| future `HackRF One` | `TBD`           | likely `C3 RF` or larger compatibility study |

## Design Rule

If a cartridge is supposed to be native, do not solve it with a compatibility faceplate unless you are willing to admit it should be `C3`.
