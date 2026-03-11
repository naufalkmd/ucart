# C1 Utility Nav Wokwi Test Plan v0.1

## Purpose

Define what can be usefully prototyped in Wokwi for `C1-001 Utility Nav` before any hardware is built.

This plan is for the native cartridge path only.

It is not a simulation plan for `RTL-SDR`, `Proxmark3`, RF performance, or real GNSS reception.

## Goal

Use Wokwi to de-risk the native cartridge logic by proving:

- `RP2040` firmware structure
- cartridge present and ID handling
- `UART` behavior
- `I2C` behavior
- basic `RTC` interaction
- mocked `GNSS` data handling

## What Wokwi Should Cover

Wokwi is useful here for:

- `RP2040` firmware loop structure
- GPIO-backed cartridge detect simulation
- GPIO-backed cartridge ID simulation
- `I2C` peripheral scanning and basic transactions
- `RTC` read and write behavior
- UART parsing and logging for mocked `GNSS` data

## What Wokwi Should Not Be Asked To Prove

Do not use Wokwi results as proof for:

- real `RTL-SDR` USB behavior
- real `Proxmark3` USB behavior
- RF performance
- real GNSS RF reception
- hot-swap behavior
- power integrity under real cartridge load

## Recommended Wokwi Model

Build one simple virtual setup around:

- `RP2040` or Raspberry Pi Pico target
- one `RTC` device on `I2C`
- one mocked `GNSS` data source on `UART`
- GPIO inputs for `CART_PRESENT_N`, `CART_ID0`, and `CART_ID1`
- optional logic analyzer attachment for signal sanity checks

## Simulation Architecture

```text
RP2040 / Pico firmware
        |
        +-- GPIO input for `CART_PRESENT_N`
        +-- GPIO input for `CART_ID0`
        +-- GPIO input for `CART_ID1`
        +-- I2C bus -> RTC model
        +-- UART RX -> mocked GNSS NMEA source
        +-- UART TX -> debug console output
```

## Suggested Test Firmware Responsibilities

The Wokwi firmware should do these things on boot:

1. read `CART_PRESENT_N`
2. read `CART_ID0` and `CART_ID1`
3. initialize `I2C`
4. scan the `I2C` bus
5. probe the `RTC`
6. start the `UART` receiver for mocked GNSS input
7. print a compact status report over the debug console

## Recommended Virtual Peripherals

### RTC

Use a simple `I2C` RTC model supported by Wokwi.

The exact chip family is less important than proving the firmware flow.

### GNSS

Do not wait for a perfect GNSS simulator.

Use one of these simpler approaches:

- a second serial source that emits fixed NMEA-like strings
- a firmware-side mock stream generator that exercises the same parser path
- a scripted or timed UART feed if you later add a richer simulator harness

The goal is to prove parser behavior and state handling, not satellite physics.

## Core Test Cases

### Test 1: Present Detect Logic

Simulate:

- cartridge absent
- cartridge present

Pass condition:

- firmware reports the expected state cleanly
- no ambiguous interpretation of active-low logic

### Test 2: Cartridge ID Logic

Simulate all intended ID combinations for the native test path.

Pass condition:

- firmware reads and reports the strap values correctly
- status output is stable across resets

### Test 3: I2C Bus Bring-Up

Simulate:

- expected RTC attached
- optional second device if you want to mimic future GNSS-over-I2C work

Pass condition:

- firmware scans and reports the expected addresses
- error handling is clean when the bus is empty or a device is missing

### Test 4: RTC Read and Write Path

Simulate:

- reading time from the RTC
- writing a known value if the model supports it

Pass condition:

- firmware can complete a full RTC interaction path without blocking the rest of the system

### Test 5: Mock GNSS UART Input

Simulate:

- fixed valid NMEA-like lines
- malformed lines
- silence timeout

Pass condition:

- parser accepts good data
- parser rejects bad data cleanly
- firmware keeps running when no GNSS data appears

### Test 6: Boot Status Report

Simulate a normal boot with cartridge present and expected peripherals attached.

Pass condition:

- console output clearly reports present state, cartridge ID, RTC status, and GNSS parser state

## Recommended Console Output Format

Keep the Wokwi firmware output compact and machine-readable enough to reuse later.

Example fields:

- `present`
- `id0`
- `id1`
- `rtc_ok`
- `rtc_addr`
- `gnss_seen`
- `gnss_fix_mock`

## Suggested Deliverables

The Wokwi stage should produce:

- one `diagram.json` or equivalent Wokwi wiring definition
- one minimal firmware source file
- one short test note recording which simulated cases passed

## Practical Design Rules

- keep the first model small
- use mocked `GNSS` input instead of chasing realism
- optimize for deterministic firmware behavior, not flashy simulation
- if a behavior can be tested later on the real breakout with less effort, defer it

## Exit Condition

This plan is complete when the native cartridge firmware flow is stable enough that hardware bring-up can focus on electrical problems instead of basic application logic.
