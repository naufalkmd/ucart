# Mechanical Layout v1

## Design Intent

The enclosure should behave like a cartridge host, not a multi-bay module rack.

## Layout Model

```text
Rear or top view

+---------------------------------------------+
|                 uCart Host                  |
|                                             |
|   top edge -> [ primary female slot ]       |
|                                             |
| power + control spine inside host body      |
+---------------------------------------------+

External edges

USB-C power | host/service link | debug access | status LEDs
```

## Mechanical Standard Rules

- one primary cartridge opening is visible and easy to understand
- cartridges insert from the top edge in one consistent direction
- connector contact area stays protected inside the host and mates near end-of-travel
- cartridge face should expose module-specific antennas or service ports as needed
- retention should feel deliberate and repeatable, not loose friction-fit only
- keep the center of mass close to the host body
- keep RF-sensitive regions clear of unnecessary metal and switching noise

## Suggested Host Construction

- structural bracket to uConsole body
- removable host shell with captive screws
- internal guide rails for cartridge alignment
- recessed internal card-edge style backplane connector
- labeled service access for power and debug

## Practical Interpretation

From the outside, every cartridge should feel like part of one family even if the electronics behind the shell differ later.
