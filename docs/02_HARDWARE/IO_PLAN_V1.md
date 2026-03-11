# I/O Plan v1

## External Host Ports

- 1x `USB-C` power input for `uCart Host`
- 1x host or service link to uConsole
- 1x debug access point for UART and maintenance
- cartridge face supplies module-specific antenna or service access

## Internal Host Connectivity

### C1 Host Backplane

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

- `C1-001 Utility Nav` -> native compact cartridge using the `C1` backplane directly
- `C3-001 RTL-SDR Scout` -> compatibility cartridge adapting an `RTL-SDR`-class USB device onto the `C1` host backplane
- `C3-002 Proxmark3 Easy RFID` -> compatibility cartridge adapting a `Proxmark3 Easy`-class device onto the `C1` host backplane

## Deferred Mapping

- future native `LoRa/GNSS` modules -> `C1` or `C2` study
- `C3-003 HackRF One` -> future compatibility study

## Current Direction

- use a protected internal card-edge style connector for the `C1` host backplane
- use top-loading cartridge insertion into the host
- let `C3` cartridges bridge awkward devices onto the host without redefining native `C1`

## Open Decisions

- confirm or revise provisional C1 shell dimensions after physical board mockups
- select the exact production connector family from the `C1` shortlist after physical tests
- host link method between uConsole and `uCart Host`
- whether `RTC` lives in every host or only in a utility cartridge
- whether `GNSS` should be cartridge-based or fixed in the host
