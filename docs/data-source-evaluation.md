# Data Source Evaluation

## Current Strategy

Phase 1 will begin with the Premier League as a controlled pilot before expanding to Serie A, Bundesliga, La Liga, Ligue 1, and other competitions.

The immediate goal is not to find one perfect source. Instead, different sources may serve different roles in the project.

## Current Source Shortlist

| Source | Planned Role | Notes |
|---|---|---|
| FBref | Main Phase 1 player-season data candidate | Broad aggregate player statistics; likely starting point for representation work |
| Premier League official site | Validation reference | Useful for checking official league/player totals and definitions |
| FotMob | Secondary/reference source | Rich player and match information; may be useful for validation or enrichment |
| StatsBomb Open Data | Event-level experimentation | Useful for learning how higher-level metrics are constructed from actions and locations |
| DataMB | Product/methodology reference | Useful for studying percentile-based player comparison and presentation |
| Opta Analyst | Product/methodology reference | Useful as a benchmark for professional comparison tools and role-aware analysis |
| Hudl | Future professional-grade reference | Appears useful but currently excluded because the project is prioritizing free data |

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
                 FBref
            Player-season data
                    │
                    ▼
        Clean + engineer features
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    PL Official           FotMob
    Validation          Validation /
                         enrichment

                    +
                    │
                    ▼
           StatsBomb Open Data
         event-level experimentation
```

DataMB and Opta Analyst will be treated primarily as methodology and product references rather than assumed raw-data providers.

## Current Open Question

Before committing to a final dataset, determine which variables are actually useful for describing how defenders, midfielders, and forwards play.
