# Visual Design — Pattern Reference

Hierarchy, spacing, type and colour decide what people notice first. Review them as
behaviour: what does someone look at, misread or miss because of the visual choices?

## Hierarchy

- **Three levels:** primary (the main action or information, one per view), secondary
  (supporting content), tertiary (metadata, hints, timestamps).
- **Weight and colour before size.** De-emphasise supporting text with a lighter grey or
  weight before enlarging the main element.
- **Emphasis and markup are separate decisions.** A heading level doesn't fix a visual size.
- **Buttons:** one filled primary per view; secondary outlined or subtle; tertiary text-only.
- *Risk: when everything is emphasised, people scan longer and miss the one action that
  matters.*

## Spacing

- Base unit 4 or 8 px; scale 4, 8, 12, 16, 24, 32, 48, 64, 96. Pick from the scale, never by eye.
- Forms: 4 px input → help text, 8 px label → input, 24 px between groups.
- **Space between groups larger than space inside them**, or labels attach to the wrong field.
- Start with too much whitespace, then reduce. Squint test: related items merge into one
  shape, groups stay apart.
- Density follows the job: data tables and dashboards dense; onboarding and empty states roomy.
- Before adding a border, try a background change, more space or a shadow.

## Type

| Body text on screen | Value |
|---|---|
| Size | 15–25 px; product UI body rarely below 16 px |
| Line spacing | 120–145% of the size (headings about 1.2) |
| Line length | 45–90 characters, spaces included |
| Paragraphs | Space between or first-line indent, not both |

- A small scale (e.g. 12, 14, 16, 18, 20, 24, 30, 36, 48) and two or three sizes per component.
- Weights with a job: regular body, medium labels, semibold buttons and subheads, bold headings.
- Bold or italic sparingly, never together. Underline only links. All caps under a line,
  with 5–12% extra letter spacing.
- Interface text is scanned: front-load the words that matter. Reading rules apply to help,
  empty states and anything over two lines.
- *Risk: lines over ~90 characters on wide screens make people lose their place and skim.*

## Colour

- **Roles, not swatches:** 9+ neutrals (text, borders, backgrounds), 5–7 shades of a primary
  (actions, links, selection), status colours always paired with text or an icon.
- Saturated colour only where it means something. Tint greys slightly towards the brand hue.
  Use a grey from the scale for secondary text, not reduced opacity.
- **Contrast:** text 4.5:1; controls, their states and meaningful graphics 3:1 against
  adjacent colours (WCAG 1.4.11).
- **Never colour alone** (WCAG 1.4.1): errors need a message and icon; valid/invalid
  outlines need another cue; links in text need an underline or 3:1 against the text.
- Check charts and status sets in greyscale.

## Review questions

1. What is the one primary thing on this view? Can you see it in two seconds?
2. Do groups survive the squint test?
3. Are all spacing values on the scale?
4. Is body text inside 45–90 characters a line and 120–145% line spacing?
5. Does every colour have a role, and does every coloured signal also have text or a shape?

Sources: *Refactoring UI* (digest) · Matthew Butterick, *Practical Typography* · WCAG 2.2
1.4.1, 1.4.3, 1.4.11.
