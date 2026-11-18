# Touch and Mobile — Pattern Reference

Design for fingers and thumbs, not for "touch". Grips change constantly, and accuracy
depends more on where on the screen a target sits than on which hand is used.

## How people hold phones (field observation, 1,333 people, 780 touching the screen)

| Grip | Share | Detail |
|---|---|---|
| One hand | 49% | Right thumb 67%, left 33% |
| Cradled | 36% | One hand holds, the other taps (thumb 72%, finger 28%) |
| Two hands | 15% | Nine in ten in portrait |

Grips shift every few seconds. Early thumb-reach diagrams were withdrawn by their author;
plan for accuracy by zone instead of fixed reach zones.

## Accuracy by zone

| Zone | Accuracy | Target spacing |
|---|---|---|
| Centre | Highest | About 7 mm centre to centre |
| Left and right edges | Slightly lower, same for both hands | Full-width list rows over small icons and checkboxes |
| Top and bottom edges | Lowest; slower, less confident | 10–12 mm between selectable items |

Edge misses come from lift-off: a tap registers on release, and at low thumb angles the
contact point drifts.

## Rules

- Don't put rare or risky actions at hard-to-hit edges just because one-handed use is common;
  don't design only for one-handed use either.
- Keep tappable items away from tab bars, or separate them with space or non-tappable labels.
- Leave space below the last list item so people can scroll it to a comfortable position.
- Separate visible target, touch target and interference. Fix misses with spacing before size.
- Check the smallest supported screen: a bar of five icons may only fit four.
- Treat the viewport, not the page, as the design space; mobile browser chrome moves edges.
- Test on a real device in every likely grip, and check what fingers cover.

## Review questions

1. Which targets sit in the top or bottom edge, and are they 10–12 mm apart?
2. Are side controls full-width rows rather than small icons or checkboxes?
3. Is anything tappable crowding the tab bar?
4. What does the hand cover during the main task?

Sources: Steven Hoober, "How do users really hold mobile devices?" and "Design for fingers
and thumbs instead of touch" (UXmatters).
