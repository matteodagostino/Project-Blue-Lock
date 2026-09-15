# Current Project Status

_Last updated: 2026-09-15_

## Current Phase

Project Blue Lock is still in **Phase 1 — Player Representation**. The current question remains:

> **Can we create a meaningful quantitative representation of how a professional soccer player plays?**

The most recent work shifted the short-term prototype from searching only for ready-made aggregate player statistics toward learning how to engineer useful passing features directly from event-level data.

## Latest Experiment — StatsBomb Open Data

StatsBomb Open Data was tested as an event-level source using the `statsbombpy` Python package.

The available Premier League seasons were audited and the **2015/16 Premier League** was selected as the first controlled test dataset:

- `competition_id = 2`
- `season_id = 27`
- 380 matches available

The first test match selected was:

- **Chelsea vs Arsenal**
- **2015-09-19**
- `match_id = 3754217`

The match event data was loaded successfully. Event types were inspected and the match contained **1,046 Pass events**. Pass events were isolated into a separate DataFrame and pass-specific fields were reviewed.

The raw match event table was exported to CSV and reloaded with pandas for inspection. Initial data-quality checks were started for data types, missing values, and duplicate rows.

## Key Realization

The raw StatsBomb event table is not directly useful as a scouting output by itself. Its value is that it contains the spatial and contextual information needed to engineer our own football features.

Each pass can be treated as a vector from a start coordinate `(x1, y1)` to an end coordinate `(x2, y2)`.

This creates the opportunity to derive features such as:

- pass starting location
- pass ending location
- defensive / middle / attacking third
- forward, lateral, or backward movement
- pass distance
- progressive passes
- final-third entries
- penalty-area entries
- long passes
- completion status

The same approach can later be extended to carries and other event types.

## Current Intended Spatial Passing Pipeline

```text
StatsBomb raw events
        ↓
Filter Pass events
        ↓
Split start/end coordinates
        ↓
Engineer spatial features + classifications
        ↓
Save clean passes_enriched.csv
        ↓
Validate on a football pitch
        ↓
Generalize across all 380 Premier League matches
        ↓
Aggregate into player-level passing profiles
        ↓
Interactive scouting interface
```

## Candidate Analytical Columns

The first enriched pass-level table is expected to contain fields such as:

```text
match_id
player
team
minute
second
start_x
start_y
end_x
end_y
delta_x
delta_y
pass_length
completed
start_third
end_third
pass_direction
progressive_pass
final_third_entry
penalty_area_entry
long_pass
```

Exact definitions for progressive passes, long passes, and zone-entry metrics should be selected deliberately and documented rather than chosen arbitrarily.

## Visualization Direction

The desired product is now more **pitch-first** than a traditional KPI-heavy dashboard.

The central interaction should resemble a player event view such as SofaScore:

- the football pitch occupies most of the interface;
- the user selects a player;
- the pitch redraws to show only that player's passes;
- selectable attributes such as All Passes, Progressive, Long, Final Third, or Into Box filter what is drawn;
- supporting metrics remain secondary to the spatial visualization.

Power BI is no longer assumed to be the final visualization tool. The current leading workflow is:

1. **Python + mplsoccer** for validating StatsBomb coordinates and football logic.
2. Evaluate **Streamlit + Plotly** for the interactive application.
3. Compare against Tableau / Power BI only after the spatial prototype is working.

## Exact Resume Point

The next task is **Spatial Passing Pipeline v0.1** using only Chelsea vs Arsenal.

Start by transforming StatsBomb's nested coordinate fields:

```text
location → start_x, start_y
pass_end_location → end_x, end_y
```

Then calculate / validate:

```text
delta_x
Delta_y
pass distance
pitch-third classifications
```

Before defining progressive passes or other higher-level metrics, plot one selected player's passes on a StatsBomb-format pitch and verify that the spatial coordinates are correct.

Once the one-match transformation works reliably, package it as reusable Python functions and apply the same pipeline across the full 2015/16 Premier League season.
