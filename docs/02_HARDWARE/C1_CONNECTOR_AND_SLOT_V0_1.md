# C1 Connector and Slot v0.1

## Purpose

Select a realistic connector direction and slot concept for the first `C1` host backplane and slot.

This document is intentionally pragmatic. The goal is not the most elegant connector on paper. The goal is a connector and slot that can survive repeated user insertion without turning `uCart` into a high-speed backplane project.

This slot services direct native `C1` cartridges and the first `C3` compatibility cartridges in v1.

## Decision Summary

### Recommended v0.1 Direction

Use a protected internal card-edge style connector with guide rails and top-loading insertion.

Interpretation:

- cartridge shell stays visually consistent
- cartridge internals terminate on a small carrier PCB with edge fingers
- the host hides the mating socket inside the slot
- the user never directly touches the signal contacts

### Why This Wins for v0.1

- closest match to the cartridge mental model
- easy to explain visually
- simpler than a precision mezzanine docking scheme
- more repeatable than pogo-pin-only concepts
- fits the actual `C1` signal set well enough

## Evaluation Criteria

The connector and slot need to support:

- repeated user insertion and removal
- `USB 2.0`
- `5V` power at useful cartridge current
- `3.3V`, `UART`, `I2C`, and ID signals
- protected contacts inside the host
- low assembly pain for the first prototypes

## Candidate A: Card-Edge on Internal Carrier PCB

### Description

Each cartridge contains a carrier PCB that terminates in plated edge fingers.

The host contains a recessed mating card-edge socket.

### Pros

- most natural cartridge feel
- simple guide-rail integration
- easy to key mechanically
- good visual consistency across cartridges
- lets stock modules ride on an internal adapter instead of redefining the shell

### Cons

- cartridge internals need a carrier/interposer PCB even for stock tools
- edge plating quality matters
- connector wear still needs validation over repeated insertion cycles

### Recommended Physical Baseline

- `1.6 mm` cartridge edge PCB thickness
- at least `20` physical contacts even though `C1` currently needs `16` logical signals
- extra contacts should go to `GND` and `5V` margin first, not feature creep
- connector recessed inside the host slot with rail guidance before electrical mating

### v0.1 Recommendation

Recommended.

## Candidate B: Shrouded Board-to-Board Connector

### Description

A rigid mezzanine-style connector mates when the cartridge reaches the end of travel.

### Pros

- compact
- clean internal packaging when alignment is perfect
- can support controlled contact sequencing depending on family

### Cons

- less tolerant of user-driven insertion error
- harder to guide without a precise shell and rail system
- more likely to become fragile or annoying in early prototypes
- feels less like a cartridge and more like precision assembly

### v0.1 Recommendation

Not preferred for first prototypes.

Keep as backup only if card-edge sourcing or durability becomes a real blocker.

## Candidate C: Pogo-Pin or Magnetic Dock

### Description

Spring contacts or magnets provide electrical mating when the cartridge is pushed into place.

### Pros

- visually clean when done well
- forgiving for some low-speed contacts

### Cons

- worse confidence for repeated user insertion at the required power budget
- contact contamination becomes a practical problem
- alignment and retention become coupled problems
- does not match the cartridge feel as cleanly as it looks on paper

### v0.1 Recommendation

Reject for the main `C1` slot.

## Slot Concept

### Recommended Insertion Direction

Top-loading insertion into a rear-mounted host body.

Interpretation:

- the host sits behind or above the back of uConsole
- the user inserts the cartridge downward from the top edge
- the visible cartridge face remains accessible for labels and antenna exits

### Why Top-Loading

- strongest cartridge mental model
- easiest to understand visually
- rail alignment is straightforward
- gravity helps seating instead of fighting it
- host shell can protect the connector better than a shallow side opening

## Mating Sequence

The slot should behave like this:

1. cartridge enters guide rails
2. shell and rails constrain lateral error
3. cartridge reaches hard end-stop
4. connector mates near the end of travel
5. latch or detent locks cartridge in place

Do not let the connector itself absorb all insertion force.

## Retention Concept

Recommended v0.1 retention:

- guide rails on both cartridge sides
- positive end-stop inside the host
- simple spring latch, thumb latch, or screwless detent near the top edge

Not recommended for v0.1:

- loose friction only
- exposed connector with no rails
- hidden fasteners required for every swap

## Keying Strategy

Use mechanical keying before electrical cleverness.

Recommended v0.1 approach:

- asymmetric rail geometry or slot wall shape
- optional edge-notch asymmetry on the carrier PCB
- cartridge face markings for orientation

Do not rely on labels alone to prevent reverse insertion.

## Recommended Next Prototype Rule

Prototype the host around the recommended card-edge concept first.

If the first mechanical mockup shows unacceptable insertion feel or connector stress, revise the connector family before changing the shell philosophy.

Connector-family narrowing and build staging are documented in `C1_CONNECTOR_SHORTLIST_AND_PROTOTYPE_PLAN_V0_1.md`.

The first printable geometry targets are documented in `C1_SLOT_AND_SHELL_MOCKUP_SPEC_V0_1.md`.
