---
name: "data-visualization"
description: "Choose, design and review charts, dashboards and data visualizations using evidence-based rules — chart selection by purpose, chart styling, colour, dashboard layout and dataviz accessibility. Use whenever the user asks which chart to use, to review a chart or dashboard, to design a KPI/analytics/report view, or about chart colour or legibility — even if they only say \"this graph looks off\" or \"how should I show this metric\". Trigger with \"chart\", \"graph\", \"dashboard\", \"KPI\", \"metric\", \"data viz\", \"visualization\", \"legend\", \"axis\", \"colour scale\", \"report view\", \"analytics page\"."
---

# Data Visualization Skill

For choosing, designing and reviewing charts, dashboards and analytics views in B2B SaaS
products. Works in the same three modes as the interaction design skill:

- **CHOOSE / CREATE** — pick the chart for a metric and spec it
- **REVIEW** — audit an existing chart or dashboard with structured findings + fixes
- **SUGGEST** — 2–3 distinct ways to show the same data, with a recommendation

The unifying principle:
> A chart is an opinion about the data, not the data itself. Every element either helps
> the reader make the decision the chart exists for, or it is clutter.

Frame every finding as **what the reader concludes** and **what the business pays** when
they conclude wrongly — not as a styling preference.

---

## Step 0 — Start from the decision, not the data

Before any chart: *what decision does the reader make with this?* A sales manager looking
at pipeline needs three answers (on track? which deals need attention? what changed?) —
maybe four charts, not fifteen. If a large swing in the number would not change what the
reader does, the chart should not exist.

Also ask: who reads it (first-time or daily?), on what device, and whether the job is
**monitor** (is everything OK?), **diagnose** (why?) or **prove** (show this to my manager).
Each job needs different design decisions; a dashboard built for one breaks the others.

---

## 1. Choosing the chart

Identify the **purpose** first, then the **data types** (categorical / numeric, how many
variables), then check the result and simplify.

| Purpose | Default | Also good | Avoid |
|---|---|---|---|
| **Single number** | plain number + previous-period indicator; sparkline for trend | bullet chart vs target | plotting one value as a bar/pie |
| **Change over time** | line (irregular data → add markers) | column for few periods; slope for 2–3 points; area for totals only; fan for projections | area to compare components; many lines (>5) without highlighting |
| **Magnitude / comparison** | bar (long labels) or column; **axis must start at zero** | dot/lollipop when zero is meaningless; grouped bar for 2 categories (max ~2 series) | radar, radial bars, 3D, pictograms for non-integers |
| **Ranking** | ordered bar/column | lollipop, dot strip, slope (rank change), bump chart | unsorted bars |
| **Part-to-whole** | stacked bar (people judge length better than angle) | pie/donut **≤5 slices** with distinct proportions, state what the whole is; treemap for hierarchy; waffle for %; waterfall when parts are negative | pie with many slices; stacked bars when segment comparison matters (baselines shift — label every segment or split) |
| **Distribution** | histogram (numeric) / bar (discrete) | box plot or violin to compare groups; strip/swarm for small n; cumulative curve for inequality | box plots for tiny samples |
| **Relationship** | scatter (max 3 variables) | bubble (size = 3rd var), connected scatter (time), heatmap (two categoricals), line + column (amount vs rate) | dual axis unless unavoidable — easily misread |
| **Deviation** | diverging bar from a reference | diverging stacked bar (survey agree/disagree), surplus/deficit filled line | — |
| **Flow / process** | funnel for stage conversion | Sankey for multi-path flow, waterfall for sequential change, Gantt for schedules | chord/network unless the audience is expert |
| **Spatial** | choropleth with **rates/ratios** (never raw counts) | proportional symbol for counts; hex/dot density; cartogram when area misleads | choropleth of totals (large sparse areas dominate) |

**18 charts cover most dashboards:** single value, value + indicator, bullet, table, line,
sparkline, bar, histogram, box, pie, stacked bar, stacked area, scatter, bubble, grouped bar,
heatmap, bubble map, choropleth. Start there. Try basic before uncommon before advanced.
Prefer **several simple charts (small multiples)** over one complex one. Sometimes a table,
a sentence or a single number is the right visualization.

**Category limits:** >5–7 categories becomes hard to read quickly — group the tail into a
grey "Other".

---

## 2. Chart design rules

**Less, but better — show the data first.**
- Remove borders, drop shadows, bevels, keylines, decorative icons. Maximise data-ink.
- Gridlines and ticks: only enough to show range — usually **~5**, light but visible.
  Don't extend gridlines beyond the data (implies a continuing range).
- Too much data → small multiples with **shared scales**, not one crowded chart.
- Context series in light grey; **one highlight colour** + heavier weight for the series
  the reader should look at.

**Axes.** Bars and columns start at zero with a strong baseline, always. Lines may start
above zero *if* the baseline is removed and the range is obvious; aim for the data to fill
~two-thirds of the vertical space so variation is visible. Mark key dates/thresholds on the
axis; show only relevant tick labels.

**Labels over legends.** Label data directly wherever possible (end of line, on the bar).
Every legend lookup is a micro-interruption. Use dotted leader lines for awkward labels.
Markers only on first/last values, notable events, or sparse data.

**Titles say what to see.** "Churn rose 3 pts after the pricing change", not "Churn by
month". Sub-title states scope: timeframe, population, unit. Source line below.
Annotate the event the reader needs (launch date, target line, projection shaded).

**Context on every number.** "12%" means nothing; "12%, up from 8%, target 15%" is a
story. Benchmarks, thresholds and previous period belong *in* the chart.

**Specific chart cautions.**
- *Line charts:* don't connect unrelated snapshots — a line implies a trend that may not
  exist. Reduce line weight for dense data.
- *Stacked bars for proportions:* parts must sum to 100%; one highlight segment + labels.
- *Donut:* 2 ideal, 3–4 max; say what the whole represents; balanced ring thickness.
- *Dual axis:* only when the two series genuinely belong together; label both axes loudly.
- *Tables:* align numbers right, consistent decimals, minimal rules, sortable when long.

**Typography (relative scale, adapt to product).** Title ≈ 18 bold; explanatory ≈ 14;
axis/labels/source ≈ 12 in mid-grey; annotations 12 with 10 for secondary. Sans serif,
sized for the viewing device — nobody should squint.

---

## 3. Colour

- **Meaning first.** Colour encodes something or it's grey. Keep the same colour meaning
  across every chart in a product — never reassign.
- **Vary lightness, not just hue.** Colour-blind readers confuse colours of equal
  *lightness* — saturation doesn't save them. About 8% of men of Northern European descent
  and 0.5% of women have red–green colour vision deficiency (about 4–5% of men of Asian
  descent). Red isn't a reliable alarm; red-purple reads as blue; pink, turquoise and grey
  merge for green-blind readers. Test both protan and deutan simulations.
- **Contrast:** WCAG 2 AA is the floor; use **APCA** to choose between options, because it
  accounts for font weight and size. Every colour token must pass in every theme.
- **Categorical:** distinct hues of similar lightness and saturation so none shouts;
  comfortable up to **5**, with caution to 10, beyond that use direct labels or facets.
  Related series (daily + rolling average) share a hue, the important one darker.
- **Sequential** scale for one-directional magnitude; **diverging** for data with a
  meaningful midpoint (above/below target, positive/negative); **classed** (binned) when
  readers compare to thresholds, **unclassed** when they need the continuous gradient.
- **Never rainbow.** Use perceptually uniform ramps (viridis, magma, cividis). Don't start
  a ramp darker than its background. Red–green pairs only with a second cue.
- **Culturally loaded colours** (red = bad, green = good) are reserved for when they mean
  that; users read red/green/yellow as bad/good/average whether you meant it or not.
- **Fewer colours**: grey out everything that isn't the point. Ten ways to reduce the
  palette before adding an eleventh colour.
- **Sensitive categories** (gender, ethnicity, regions): avoid pink/blue defaults and
  stereotyped mappings; pick neutral, distinguishable hues.
- Test every palette for deuteranopia and on a projector / poor monitor / print (pink
  prints as red; light colours wash out).

---

## 4. Dashboards

**A — Accurate.** Readers must trust it or they won't use it. Show *last updated* and
refresh cadence; flag broken data loudly; put metric definitions beside the visual, not in
a tooltip. Zero baselines for bars; honest ranges for lines.

**C — Clear.** Descriptive titles, axis titles, category labels — a chart that needs an
explanation outside itself is incomplete. Most important information **top-left**, least
bottom-right. Align everything; misaligned panels pull attention for no reason.

**E — Empowering.** Judged after launch: is it viewed regularly, and would a big change in
the number lead to an action? If not, remove it or rebuild it around a decision.

**S — Succinct.** Everything the reader must compare is visible at once — scrolling and
tabs force recall, and working memory fails under time pressure. Nothing important below
the fold. Only charts relevant to this dashboard's purpose; drill-down lives in a linked
second dashboard, not in more panels.

**Should it be a dashboard at all?** Fewer than one in ten adults aged 16–65 in the US have
proficient numeracy, and people read single values far more easily than relationships or
trends. Dashboards earn their place for expert analysts. For most B2B and B2C users,
**deliver the insight in context instead** — a sentence where the decision happens ("3
campaigns stopped sending yesterday") beats a chart they have to interpret.

**Operational or analytical?** Operational dashboards (monitor now, act fast) are for
people running a process: few widgets, status first, live. Analytical dashboards (explore,
compare over time) are for people investigating: filters, drill-down, history. Set
defaults **by role**, rather than relying on each user to customise. Design the dashboard
**last**, after the questions are known.

**Four trade-offs — minimising one stresses the others:** screen space, number of pages,
level of abstraction, and amount of interaction. Fit-to-screen means more abstraction or
interaction; no interaction means more pages or scrolling. Choose deliberately.

**Meta-information is part of the design:** data source, description, last update and
refresh cadence, disclaimers, and annotations for events that explain a spike. Without it,
readers can't trust the number.

**Builder-style dashboards** (users assemble their own): widgets snap to slots; offer
templates and a blank state with two clear actions; let people try it with sample data;
export both a read-only view (PDF) and raw data (CSV); time presets plus a custom range;
highlight and drill down across charts.

**Layout rules.**
- Group related metrics into zones (and tint zones subtly if it helps); two views of the
  same metric (current value + trend) sit together; stacked time charts share a time axis.
- Around **six chart types** is the ceiling — beyond that usage drops sharply.
- KPIs get **equal visual weight** unless you deliberately anchor on one.
- Comparisons side by side, never behind toggles. Tabs only for mutually exclusive content.
- State scope (period, segment, filter) persistently in titles and sublabels, not only in
  a filter bar the reader scrolled past.
- **Accidental grouping:** proximity and shared colour make readers infer relationships —
  separate unrelated metrics with space, not lines.
- Confirm the target device and aspect ratio (laptop, TV wall, phone) before composing.
- Pair colour with shape, text or position; colour-only status fails colourblind readers
  and grayscale print.

---

## 5. Accessibility

Accessible charts are a stress test: fixes for screen-reader and colourblind users almost
always improve the chart for everyone under distraction, small screens and bad projectors.

**Perceivable**
- Text and marks meet WCAG contrast (AA minimum) against the background.
- Never colour alone: add pattern fills (subtle), shape, direct labels or position.
- Avoid bright, saturated fills — they tire readers and hurt focus; bright labels on bright
  fills are unreadable.
- Show values as text where precision matters; a bar without a number is only a comparison.

**Operable**
- Anything available on hover must be available by keyboard and touch; **no hover-only
  information** (tooltips are supplementary). Support arrow-key movement through series.
- Key summaries and thresholds visible without interaction.

**Understandable**
- Title + plain-language takeaway + units on both axes. Explain the chart type if unusual.
- Legend placed before the data in reading order; each swatch paired with text.
- Keep layouts consistent across panels so readers learn once.

**Robust / assistive**
- SVG/canvas charts need explicit structure: `role="img"` with a title and description that
  state the conclusion for simple charts; for complex charts, read the total and link an
  accessible data table that keeps the chart's context (category + value together).
- DOM order = reading order. Hide visual duplicates off-screen, not with `display:none`.
- Test with a real screen reader (VoiceOver/NVDA) across browsers — support differs.

**Quick audit (Chartability shortlist, ~30 min):** contrast · colour-only encoding ·
text alternatives · keyboard operability · hover dependence · labels and units · reading
order · data table alternative · consistent layout · respect for OS/browser settings.

---

## Review output format

```
❌ ISSUE: [Label]
What's happening: [the chart/layout choice]
What readers conclude: [the wrong takeaway or the thing they can't do]
Business cost: [wrong decision / missed signal / support question / distrust of data]
Fix: [specific — chart type, encoding, label text, layout move]
Evidence: [FT / London / Datawrapper / ACES / WCAG / Calabro]

✅ STRONG: [Label] — why it works
```

End with a **priority stack** of the three fixes that most change what readers conclude.
If the dashboard has no identifiable decision, say so first — layout polish is pointless
until it does.

---

## Sources

- Financial Times *Visual Vocabulary* (chart taxonomy, 9 purposes) · Chartio / Atlassian
  *How to choose the right data visualization*
- Greater London Authority *City Intelligence Data Design Guidelines* v2 (Mike Brondbjerg)
- Datawrapper blog, *Data vis do's and don'ts* (colour, chart-specific cautions)
- dataschool.com *How to Design a Dashboard* (ACES, layout, metrics → charts)
- Trevor Calabro, *Why Your Data Dashboard Stinks* (perception failures, decision-first)
- Sarah L. Fossheim, accessible data visualization articles · Frank Elavsky, *Chartability*
  (POUR-CAF, 50 heuristics, 14 critical)
- Stephen Few (Perceptual Edge) and Nick Desbarats (*Practical Charts*) for dashboard
  fundamentals
- Wagner, Zide & Zimmers, *Are data dashboards vanity projects?* (numeracy evidence, PIAAC)
  · Benjamin Bach et al., *Dashboard Design Patterns* (IEEE VIS 2023) · Taras Bakusevych on
  operational vs analytical dashboards · Creative Navy dashboard-builder benchmark
- Lisa Charlotte Muth (Datawrapper) on colour blindness · Wise design system on APCA
- Further learning: Open Visualization Academy (Alberto Cairo, free courses incl. Elavsky
  on accessibility, Bertini on reading charts, Meirelles on information design);
  datavizproject.com for a catalogue of 160+ chart types