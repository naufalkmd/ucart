# C1 Connector Shortlist and Prototype Plan v0.1

## Purpose

Turn the `C1` slot concept into a buildable prototype path.

This document narrows the connector search and defines the prototype sequence needed before choosing a final production connector.

## Design Constraint Reminder

`C1` only needs to handle:

- `USB 2.0`
- `5V`
- `3.3V`
- `UART`
- `I2C`
- ID and present signals

That is important because it means `uCart` does not need a fancy high-speed backplane connector for v0.1.

## Shortlist Strategy

The shortlist is not a list of exact part numbers yet.

It is a list of connector families worth testing against the current shell and slot direction.

## Shortlist

### Option 1: Generic 1.6 mm Card-Edge Socket

#### Role

Primary v0.1 candidate for the real cartridge slot.

#### Why It Fits

- matches the cartridge mental model best
- fits the current top-loading slot concept
- works with a carrier PCB inside each cartridge
- enough electrical performance for `USB 2.0` and the low-speed `C1` bus

#### What to Look For

- supports `1.6 mm` PCB thickness
- at least `20` contacts
- right-angle or vertical form that fits the host body layout
- retention or wipe characteristics suitable for repeated insertion
- sourcing from more than one vendor if possible

#### Main Risk

- insertion feel and wear life are still unknown until tested physically

### Option 2: Boxed or Shrouded Card-Edge Variant

#### Role

Backup if a plain card-edge socket feels too exposed or too loose in the shell.

#### Why It Matters

- may improve alignment and connector protection
- can reduce user-visible contact exposure inside the slot

#### Main Tradeoff

- can make the host slot bulkier and harder to package

### Option 3: Shrouded Board-to-Board Connector Pair

#### Role

Fallback path if card-edge prototypes show unacceptable wear or alignment problems.

#### Why It Stays on the List

- may give more deterministic mating when the shell geometry is tight
- may be easier to source in small quantities depending on the exact form factor

#### Why It Is Not First Choice

- weaker cartridge feel
- less forgiving under user insertion error
- likely higher alignment sensitivity

## Rejected for v0.1 Main Slot

### Pogo-Pin Main Connector

Reject as the primary `C1` slot because power confidence, long-term contamination, and retention coupling are all worse than they need to be.

### FFC or Ribbon-Based Main Slot

Reject as the primary user-facing insertion mechanism.

FFC is useful inside a device, but it is the wrong fit for a user-swapped cartridge slot.

## Prototype Sequence

### Prototype 0: Electrical Breakout Proof

Goal:

Prove the `C1` signal set and power assumptions before building a true cartridge slot.

Method:

- host-side breakout board exposing all `C1` signals
- cartridge-side breakout board exposing all `C1` signals
- connect them with short jumper or ribbon links
- validate `RTL-SDR`, `Proxmark3 Easy`, and `Utility Nav` signal needs

Success criteria:

- stable `USB 2.0` enumeration
- no power instability at planned load
- working `UART` and `I2C` side paths
- cartridge ID logic behaves as expected

### Prototype 1: Raw Connector Fixture

Goal:

Test candidate connector families without the full shell.

Method:

- simple fixture plate or flat carrier PCB
- one host connector candidate at a time
- repeated insertion tests by hand
- basic `USB` and power validation during insertion cycles

Success criteria:

- connector survives repeated insertion without obvious degradation
- no intermittent power drop during static operation
- alignment is manageable without absurd precision

### Prototype 2: Mechanical Slot Mockup

Goal:

Validate the cartridge feel.

Method:

- 3D print host slot geometry with guide rails
- 3D print blank cartridge shells around the carrier PCB
- use the leading connector candidate inside the mockup
- evaluate insertion angle, latch feel, and connector protection

Success criteria:

- cartridge insertion is intuitive
- connector does not take the full insertion load
- latch and end-stop feel repeatable
- user cannot easily misinsert the cartridge backwards

### Prototype 3: First Functional Cartridge Pair

Goal:

Prove the actual host concept with real cartridges.

Suggested pair:

- `C1-001 RTL-SDR Scout`
- `C1-003 Utility Nav`

Reason:

- one USB-native stock-tool case
- one low-speed utility case
- enough variety to expose bad assumptions quickly

Success criteria:

- both cartridges detect reliably in the same host
- swap process is repeatable
- no enclosure disassembly required for normal use

## Recommended Immediate Next Build Order

1. build `Prototype 0` first
2. source `2-3` connector-family candidates for `Prototype 1`
3. print a blank host slot and blank shell for `Prototype 2`
4. only then freeze the exact production connector family

## Do Not Do Yet

- do not optimize for final industrial appearance
- do not design around `HackRF One` yet
- do not chase hot-swap polish before basic insertion reliability exists
- do not add `USB 3.x`, `HDMI`, or future-proof pins to the first prototype

## Exit Criteria

This plan is complete when:

- one connector family is clearly preferred after physical tests
- one shell and slot geometry survives practical insertion testing
- the first functional cartridge pair works in the same host
