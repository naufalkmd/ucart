# v1 Cartridge Set

## Purpose

Freeze a narrow and buildable first cartridge set for `uCart`.

## Decision

The first three cartridges are:

1. `C1-001 RTL-SDR Scout`
2. `C1-002 Proxmark3 Easy RFID`
3. `C1-003 Utility Nav`

`C1-003 Utility Nav` is a low-speed utility cartridge built around:

- `RP2040`
- `GNSS`
- `RTC`

## Why These Three

### `C1-001 RTL-SDR Scout`

Chosen first because it is:

- cheaper than `HackRF`
- lower power
- easier to cool
- easier to fit into a first cartridge shell
- enough to prove the `C1` USB-based cartridge path

### `C1-002 Proxmark3 Easy RFID`

Chosen second because it proves a second real stock-tool workflow while staying more practical for a cartridge shell than larger Proxmark variants.

### `C1-003 Utility Nav`

Chosen third because it proves the non-radio side of `C1`:

- low-speed buses
- cartridge ID and control logic patterns
- GNSS and RTC support
- a useful everyday cartridge even when no SDR or RFID tool is inserted

## Deferred From Frozen v1 Set

### `HackRF One`

Deferred because it changes too many constraints at once:

- higher power draw
- larger board size
- tougher thermal packaging
- more difficult shell design

`HackRF One` stays a strong future candidate, but it should not define the first cartridge shell.

### `LoRa`

Deferred because the board ecosystem is fragmented and the project needs a stable cartridge baseline first.

## Success Condition

`uCart` v1 is considered directionally validated when these three cartridges can be:

- inserted consistently
- detected consistently
- powered reliably
- used without cable sprawl or enclosure disassembly
