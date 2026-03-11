# Software Plan

## Host Role

uConsole remains the main compute and UI environment.

## v1 Responsibilities

- detect cartridge insertion state
- identify the inserted cartridge reliably
- enumerate USB devices behind the cartridge when present
- provide serial access to cartridge debug paths where relevant
- keep device naming predictable with udev or equivalent rules
- present a simple answer to the user: what cartridge is inserted, and is it usable

## Detection Strategy

Software should combine multiple signals where available:

- cartridge presence detect
- cartridge ID pins or ID device
- expected USB VID and PID patterns
- expected UART or I2C responses for utility cartridges

## Native Simulation Path

Before hardware exists, the native cartridge logic can be exercised in Wokwi using `C1_UTILITY_NAV_WOKWI_TEST_PLAN_V0_1.md`.

This is only for the `C1-001 Utility Nav` logic path. It does not validate compatibility USB or RF behavior.

## First Software Deliverables

- cartridge inventory script
- insertion and detection verification script
- USB verification script
- serial verification script
- cartridge status report

## v1 Detection Goal

The host should answer a simple question reliably:

"Which cartridge is inserted right now, and is it working?"
