# Current Project Status

_Last updated: 2026-10-12_

## Phase 1 — Player Representation

My guiding question is: **Can I build a meaningful quantitative representation of how a soccer player plays?**

I am currently experimenting with **event-level spatial passing data** before committing to a comprehensive player profiling or similarity system.

## Dataset and Working Tables

I am using StatsBomb Open Data through `statsbombpy` for the **2015/16 Premier League**, initially testing **Chelsea vs Arsenal (2015-09-19)**:

- Competition ID: `2`
- Season ID: `27`
- Match ID: `3754217`
- The match contains **1,046 Pass events**.

I originally exported all match events to CSV and loaded them into Pandas as `CFCvARSvGW1`. I preserve this table as the original event data. I then created `passingDF` by filtering for pass events and selecting **11 columns**: `player`, `team`, `position`, `location`, `pass_end_location`, `pass_length`, `pass_recipient`, `pass_outcome`, `play_pattern`, `minute`, and `second`.

**Data availability note:** The competition metadata returned 380 Premier League match records, but full event availability across all those matches has not been verified. I will not assume a complete 380-match event corpus until I audit it.

## Completed on October 12

1. **Prepared spatial coordinates.** I converted string-encoded lists in `location` and `pass_end_location` into actual Python lists, then created `start_x`, `start_y`, `end_x`, and `end_y`.
2. **Built pass vectors.** I calculated `delta_x` and `delta_y`, then used `np.hypot` to calculate Euclidean pass lengths.
3. **Validated distance calculations.** Across the 1,046 pass events, the mean absolute difference from StatsBomb `pass_length` was `5.193949e-07`, median `3.486958e-07`, and maximum `5.491767e-06`. This supports correct extraction and geometric consistency but does not independently verify real-world event locations.
4. **Created individual pitch maps.** Using `mplsoccer` and Matplotlib, I plotted pass arrows for Cesc Fàbregas, Mesut Özil, Theo Walcott, and Santi Cazorla. These maps show completed passes separately from other recorded outcomes.
5. **Confirmed the `pass_outcome` convention.** A null outcome generally represents a completed pass; populated values indicate another recorded outcome. I kept the source column instead of generating duplicate indicator columns.
6. **Documented the workflow in first person** in the working research notebook.

The plots render for multiple players, so I have a working **single-player passing-map prototype**. I have not yet produced a network or independently compared pass locations with match footage.

## Next Session — Build the Passing Network

My immediate goal is a **one-team Arsenal passing network** using the same Chelsea–Arsenal match:

1. Use `sb.lineups(match_id=3754217)` to inspect the Arsenal roster and shirt numbers.
2. Keep Arsenal passes with a null `pass_outcome` and identifiable `pass_recipient`.
3. Aggregate directed passer-to-recipient counts into an edge table.
4. Calculate average pass-start coordinates for each passer to create network nodes.
5. Join jersey numbers and plot a network with node positions and edge widths encoding completed pass counts.
6. Check whether substitutions, minutes played, and set pieces create misleading connections; choose sensible filters before further comparison.

**Definition reminder:** A network node at the mean pass-origin location is *not* the player's true average location in the match.

## Longer-Term Visual Product

My eventual interface should be **pitch-first**, with the soccer field occupying most of the screen and player and passing-attribute filters changing the displayed arrows or passing connections. The current preferred experimentation stack is `Python + mplsoccer`; I may later evaluate `Plotly + Streamlit` for an interactive scouting interface.

Later phases include defensive/middle/attacking-third classification, progressive-pass definitions, penalty-area entries, automated per-match processing, and meaningful player-level aggregations. Those metrics and the complete two-team network **have not yet been implemented**.

## Main Files

- [Research notebook](../notebooks/ProjectBlueLock.ipynb) — initial repository notebook; see the work log for the latest progress.
- [Work log](work-log.md) — chronological project decisions and results.
- [Data source evaluation](data-source-evaluation.md) — candidate sources, licensing considerations, and coverage caveats.
