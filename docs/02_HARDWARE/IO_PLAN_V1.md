# I/O Plan v1

## External Host Ports

- 1x `USB-C` power input for `uCart Host`
- 1x host or service link to uConsole
- 1x debug access point for UART and maintenance
- cartridge face supplies module-specific antenna or service access

## Internal Host Connectivity

### C1 Backplane

- `5V`
- `3.3V`
- `GND`
- `USB 2.0`
- `UART`
- `I2C`
- ID pins

### Host Functions

- cartridge presence detection
- cartridge ID read or classification logic
- regulated power distribution
- optional status indication and fault handling

## Frozen v1 Device Mapping

- `C1-001 RTL-SDR Scout` -> `RTL-SDR`-class USB device
- `C1-002 Proxmark3 Easy RFID` -> `Proxmark3 Easy`-class USB device
- `C1-003 Utility Nav` -> `RP2040 + GNSS + RTC`

## Deferred Mapping

- `HackRF One` -> future cartridge study
- `LoRa` -> future cartridge study

## Current Direction

- use a protected internal card-edge style connector for `C1`
- use top-loading cartridge insertion into the host

## Open Decisions

- confirm or revise provisional C1 shell dimensions after physical board mockups
- select the exact production connector family from the `C1` shortlist after physical tests
- host link method between uConsole and `uCart Host`
- whether `RTC` lives in every host or only in a utility cartridge
- whether `GNSS` should be cartridge-based or fixed in the host
