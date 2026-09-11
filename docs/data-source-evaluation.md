# Data Source Evaluation

## Current Strategy

Phase 1 will begin with the Premier League as a controlled pilot before expanding to Serie A, Bundesliga, La Liga, Ligue 1, and other competitions.

The immediate goal is not to find one perfect source. Different sources may serve different roles in the project: raw data, validation, methodology reference, or dashboard/product inspiration.

## Current Source Shortlist

| Source | Planned Role | Notes |
|---|---|---|
| xGStat | Methodology / feature / product reference | Strong Premier League player profiles and role-aware metrics, but current terms prohibit scraping/automated extraction and restrict redistribution of licensed data outside the platform. Not suitable as the raw public-GitHub dataset without explicit permission or a clearly licensed export workflow. |
| FBref | Re-evaluate as Phase 1 candidate | Previously identified as a likely player-season source. Current 2026 availability and advanced-stat coverage should be re-audited before committing to it. |
| Premier League official site | Validation reference | Useful for checking official league/player totals and definitions. |
| FotMob | Secondary/reference source | Rich player and match information; may be useful for validation or enrichment, subject to access and usage-right review. |
| StatsBomb Open Data | Event-level experimentation | Useful for learning how higher-level metrics are constructed from actions and locations. Coverage is selected rather than a complete recent Premier League season. |
| DataMB | Product/methodology reference | Useful for studying percentile-based player comparison and presentation. |
| Opta Analyst | Product/methodology reference | Useful as a benchmark for professional comparison tools and role-aware analysis. |
| Hudl | Future professional-grade reference | Appears useful but currently excluded because the project is prioritizing free data. |

## xGStat Evaluation — 2026-09-11

### Strengths

- Premier League player database with a completed 2025/26 season and current 2026/27 coverage.
- More granular position labels than broad DEF/MID/FWD groupings, including roles such as DM, CM and CAM.
- Player pages expose per-90 percentile profiles and useful Phase 1 feature families.
- Available player-profile metrics include attacking, playmaking and defending measures such as xG, xA, key passes, final-third passes, progressive passes, progressive runs, defensive duels, interceptions, successful defensive actions, recoveries, and own-half losses.
- Includes expected threat (xT), danger-zone visualisations, match-level views, player comparisons, and similar-player tools.
- xGStat documentation states that its models are built on licensed Wyscout event data, making the source methodologically more credible than an unknown scraped dataset.

### Limitations for Project Blue Lock

- Currently Premier League-focused rather than suitable for the eventual multi-league system.
- No public API or clearly documented free bulk-export path was identified during the source audit.
- xGStat's Terms and Conditions explicitly prohibit scraping/crawling or automated extraction.
- Licensed football data is restricted to use through the platform and may not be redistributed or published outside xGStat without permission.
- This conflicts with the project's goal of maintaining a reproducible public GitHub repository containing source-derived data.

### Decision

Use xGStat as a **feature-design, validation, and product-reference source**, not as the raw data source for today's extraction pipeline.

Its player-profile taxonomy is especially useful as a benchmark for how Project Blue Lock may later structure role-aware features and dashboard views.

## Source Selection Criteria

Each candidate source should be evaluated on:

- player coverage
- league coverage
- historical depth
- age information
- positional detail
- event data availability
- spatial data availability
- physical/tracking data availability
- minutes played
- stable player/team/match identifiers
- format (CSV, JSON, API, etc.)
- update frequency
- cost
- usage rights
- data quality
- missingness

## Data Granularity

The project should distinguish between three major forms of soccer data:

### Aggregate Data

Player-season or player-match summaries such as goals, assists, expected goals, passing, progressive actions, tackles, interceptions, and minutes.

### Event Data

Individual actions such as passes, carries, shots, pressures, and tackles, often with timestamps, outcomes, and pitch coordinates.

### Tracking Data

Continuous player and ball locations over time, which can support analysis of spacing, pressing, off-ball runs, acceleration, positioning, and team shape.

## Current Working Architecture

```text
                  PHASE 1
                     │
                     ▼
          Reusable raw data source
        (to be selected / re-audited)
                     │
                     ▼
         Clean + engineer features
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
     PL Official   xGStat     FotMob
     Validation   Feature /   Validation /
                  product     enrichment
                  reference

                     +
                     │
                     ▼
            StatsBomb Open Data
          event-level experimentation
```

DataMB, Opta Analyst, and xGStat will currently be treated primarily as methodology/product references rather than assumed raw-data providers.

## Current Open Question

Select a source with sufficient player-season coverage **and** reuse terms compatible with a reproducible public portfolio project, then build a small first analytical table for the 2025/26 Premier League pilot.
