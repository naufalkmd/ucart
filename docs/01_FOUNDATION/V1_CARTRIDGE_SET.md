# v1 Cartridge Set

## Purpose

Freeze a narrow and buildable first cartridge set for `uCart`.

## Decision

The first three cartridges are:

1. `C1-001 Utility Nav`
2. `C3-001 RTL-SDR Scout`
3. `C3-002 Proxmark3 Easy RFID`

`C1-001 Utility Nav` is the first native cartridge and is built around:

- `RP2040`
- `GNSS`
- `RTC`

## Why These Three

### `C1-001 Utility Nav`

Chosen first because it proves the native standard is real:

- native fit to the compact cartridge model
- low-speed buses and cartridge ID logic
- GNSS and RTC support
- useful everyday cartridge even when no compatibility tool is inserted

### `C3-001 RTL-SDR Scout`

Chosen second because it proves the compatibility layer with a simpler RF tool:

- cheaper than `HackRF`
- lower power
- easier to cool
- enough to prove RF-focused `C3` adaptation without distorting the native standard

### `C3-002 Proxmark3 Easy RFID`

Chosen third because it proves the obvious compatibility outlier:

- stock-tool workflow
- different interaction face
- still small enough to adapt without immediately forcing a second host standard

## Deferred From Frozen v1 Set

### Future Native Candidates

- purpose-designed `LoRa`
- purpose-designed `GNSS` variants
- future native modules that may fit `C1` or require `C2`

### `C3-003 HackRF One`

Deferred because it changes too many constraints at once:

- higher power draw
- larger board size
- tougher thermal packaging
- more difficult compatibility shell design

`HackRF One` stays a strong future candidate, but it should not define the first host or native standard.

## Faceplate Mapping

- `C1-001 Utility Nav` -> native compact faceplate
- `C3-001 RTL-SDR Scout` -> `C3 RF` faceplate
- `C3-002 Proxmark3 Easy RFID` -> `C3 RFID` faceplate

## Success Condition

`uCart` v1 is considered directionally validated when:

- one native cartridge and one compatibility cartridge can both be used cleanly in the same host
- native and compatibility cartridges are both detected consistently
- the system reduces cable sprawl and setup friction without lying about what is native vs compatibility
