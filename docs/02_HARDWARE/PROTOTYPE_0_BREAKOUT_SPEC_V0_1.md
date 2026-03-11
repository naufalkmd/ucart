# Prototype 0 Breakout Spec v0.1

## Purpose

Define the first electrical proof hardware for `uCart` before any real slot or cartridge shell is built.

This prototype exists to answer one question clearly:

Can the frozen `C1` signal set support one native cartridge path and the first compatibility paths without power, USB, or low-speed bus surprises?

## Scope

Prototype 0 is intentionally simple.

It includes:

- one host-side breakout board
- one cartridge-side breakout board
- one short temporary interconnect harness
- real test targets for native and compatibility use cases
- a repeatable test matrix with pass and fail criteria

It does not include:

- the final slot connector
- blind-mate insertion mechanics
- the printed shell body
- production cosmetics
- hot-swap claims

## Success Definition

Prototype 0 is successful when:

- the host-side power path holds regulation under expected cartridge load
- `USB 2.0` works reliably with the selected compatibility targets in static insertion tests
- `UART`, `I2C`, `CART_PRESENT_N`, and coarse cartridge ID behave predictably
- the native and compatibility requirements are understood well enough to move into connector fixture work

## Prototype Architecture

```text
uConsole or dev laptop
        |
        | upstream USB host link
        v
Host breakout board
        |
        | short temporary harness
        v
Cartridge breakout board
        |
        +-- native surrogate target (`C1-001 Utility Nav` dev setup)
        +-- compatibility target (`C3-001 RTL-SDR Scout`)
        +-- compatibility target (`C3-002 Proxmark3 Easy RFID`)
```

Prototype 0 proves the electrical model only.

Do not let temporary harness choices become the production slot definition.

Common-ground rule:

- the external `5V` supply and the upstream USB host path must share a valid ground reference
- the design must not back-feed external `5V` into the upstream host port

## Host Breakout Board Requirements

The host breakout board acts as a temporary stand-in for `uCart Host`.

### Required Functions

- accept dedicated `5V` input for cartridge power testing
- generate or pass through `+3V3_AUX` for low-speed logic
- expose the frozen `C1` logical signals at easy-to-probe headers
- provide upstream `USB` host connection to uConsole or a dev laptop
- provide clear test points for power rails and key control signals

### Minimum I/O

- `+5V_MAIN`
- `+3V3_AUX`
- `GND`
- `USB_D+`
- `USB_D-`
- `UART_TX_HOST`
- `UART_RX_HOST`
- `I2C_SDA`
- `I2C_SCL`
- `CART_ID0`
- `CART_ID1`
- `CART_PRESENT_N`

### Required Protection and Measurement Features

- input fuse or current-limited path on `+5V_MAIN`
- convenient current measurement point for cartridge `5V`
- test pads for `+5V_MAIN`, `+3V3_AUX`, `USB_D+`, `USB_D-`, `CART_PRESENT_N`
- jumper or switch option to disable cartridge `5V` without rewiring the whole setup

### Practical Rule

Do not power compatibility targets from a weak host-only USB path and then draw conclusions from brownouts.

Use a known-good external `5V` source for Prototype 0.

## Cartridge Breakout Board Requirements

The cartridge breakout board acts as a temporary stand-in for an inserted cartridge.

### Required Functions

- receive the full `C1` logical signal set from the host breakout
- expose simple headers or connectors for native low-speed targets
- expose a clean `USB` device connection path for compatibility targets
- provide easy strap control for `CART_ID0`, `CART_ID1`, and `CART_PRESENT_N`
- allow one board to be repurposed across native and compatibility tests

### Minimum Features

- strap header or DIP switch for `CART_ID0` and `CART_ID1`
- present-detect switch or jumper for `CART_PRESENT_N`
- `UART` header for `RP2040`-class testing
- `I2C` header for `GNSS` and `RTC` breakouts
- `USB` device connector or pigtail header for `RTL-SDR` and `Proxmark3`
- optional indicator LEDs for `5V`, `3.3V`, and present state

## Temporary Interconnect Rule

Do not run `USB 2.0` over long random dupont wires.

For Prototype 0:

- keep the host-to-cartridge interconnect short
- keep low-speed and power lines on a simple keyed header or ribbon
- route `USB_D+` and `USB_D-` over a short controlled twisted pair or very short dedicated link
- keep the total interconnect as simple as possible while still probe-friendly

## Recommended Temporary Connector Split

Prototype 0 does not need to mimic the final card-edge connector physically.

A more honest temporary split is:

### Low-Speed and Power Harness

Carry:

- `+5V_MAIN`
- `+3V3_AUX`
- `GND`
- `UART_TX_HOST`
- `UART_RX_HOST`
- `I2C_SDA`
- `I2C_SCL`
- `CART_ID0`
- `CART_ID1`
- `CART_PRESENT_N`

### USB Harness

Carry:

- `USB_D+`
- `USB_D-`
- nearby `GND` reference

This keeps Prototype 0 honest instead of pretending a bad temporary harness proves good `USB` behavior.

## Native Test Target Definition

### `C1-001 Utility Nav` Surrogate

Prototype 0 does not need the final native cartridge PCB.

It needs a dev-style surrogate that exercises the same classes of signals:

- `RP2040` or equivalent low-speed controller
- one `GNSS` breakout on `UART` or `I2C`
- one `RTC` breakout on `I2C`

### Required Native Behaviors

- host can detect cartridge present state
- host can read coarse cartridge ID straps
- `UART` link to the controller is stable
- `I2C` scan sees the expected low-speed devices
- `3.3V` rail remains stable during native activity

## Compatibility Test Target Definition

### `C3-001 RTL-SDR Scout`

Prototype 0 must prove:

- clean `USB 2.0` enumeration
- acceptable `5V` stability during device bring-up
- no unexplained disconnects during short steady-state use

### `C3-002 Proxmark3 Easy RFID`

Prototype 0 should prove:

- clean `USB 2.0` enumeration or clearly documented failure mode
- acceptable `5V` stability during idle and basic bring-up
- whether any special compatibility handling is needed before Prototype 1

## Test Matrix

### Test 1: Rail Bring-Up

Check:

- `+5V_MAIN` at host breakout
- `+5V_MAIN` at cartridge breakout
- `+3V3_AUX` at cartridge breakout

Pass condition:

- `+5V_MAIN` stays within practical USB-power expectations under planned load
- `+3V3_AUX` remains stable with native low-speed devices attached

### Test 2: Cartridge Present and ID Logic

Check:

- present signal asserted and deasserted cleanly
- each ID strap combination reads correctly

Pass condition:

- no floating or ambiguous detection state during static tests

### Test 3: Native UART Path

Check:

- host can communicate with the `RP2040` surrogate over `UART`
- basic command exchange or echo loop remains stable

Pass condition:

- no framing errors or unstable link during repeated reset and reconnect cycles

### Test 4: Native I2C Path

Check:

- host can scan the bus
- `RTC` and `GNSS` devices appear at expected addresses

Pass condition:

- consistent detection across multiple power cycles

### Test 5: `RTL-SDR` USB Enumeration

Check:

- device enumerates from the breakout setup
- device remains visible during a short steady-state session

Pass condition:

- enumeration is repeatable and power remains stable

### Test 6: `Proxmark3` USB Enumeration

Check:

- device enumerates from the breakout setup
- device remains visible during basic bring-up

Pass condition:

- either stable enumeration works, or the failure mode is clear enough to feed Prototype 1 decisions

## Recommended Measurement Order

1. bring up rails with no target attached
2. validate present and ID logic
3. validate native `UART` and `I2C`
4. validate `RTL-SDR`
5. validate `Proxmark3`

Do not start with the hardest compatibility target first.

## Minimal Prototype 0 BOM Categories

- host breakout PCB or perfboard
- cartridge breakout PCB or perfboard
- known-good `5V` supply with headroom
- `3.3V` regulator sized for native low-speed loads
- fuse or current-limited switch for cartridge `5V`
- short low-speed harness
- short dedicated `USB` link
- strap headers or DIP switch for ID and present lines
- basic test points and LEDs

## Wiring Artifacts

Prototype 0 wiring artifacts live in `hardware/prototype0/`:

- `HOST_BREAKOUT_WIRING_V0_1.md`
- `CARTRIDGE_BREAKOUT_WIRING_V0_1.md`
- `HARNESS_PINOUT_V0_1.md`

## Simulation-First Path

If parts are not available yet, do this work first:

- capture the host and cartridge breakouts in KiCad using `PROTOTYPE_0_KICAD_SCHEMATIC_CHECKLIST_V0_1.md`
- use Wokwi only for the native `C1-001 Utility Nav` firmware path, not for compatibility USB or RF proof

## Immediate Deliverables

Prototype 0 should produce these concrete outputs:

- host breakout schematic or wiring diagram
- cartridge breakout schematic or wiring diagram
- temporary harness pinout sheet
- short test log covering native and compatibility bring-up

## Explicit Non-Goals

- no hot-swap validation
- no final shell validation
- no latch validation
- no final production connector choice
- no `HackRF One` accommodation

## Exit Criteria

Prototype 0 is complete when:

- the host-side rail strategy is proven or clearly revised
- the native surrogate proves the low-speed part of `C1`
- `RTL-SDR` proves the first compatibility USB path
- `Proxmark3` is either proven or narrowed to a specific blocker
- the team can enter Prototype 1 with real connector assumptions instead of guesses
