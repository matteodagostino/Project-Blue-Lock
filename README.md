# Project Blue Lock

Project Blue Lock is a long-term data science project focused on building a data-driven soccer player discovery and profiling system.

The core idea is to represent players quantitatively, compare their playing profiles, and eventually identify young players whose performance characteristics, development trajectory, and role fit suggest that they are worth further scouting.

## Core Decision

The system is intended to help answer:

> **Which players should a scout investigate further?**

The project is designed as a decision-support tool for club recruitment analysts, sporting directors, and coaches rather than a replacement for human scouting.

## Current Objective — Phase 1

> **Can we create a meaningful quantitative representation of how a professional soccer player plays?**

The initial pilot will focus on the Premier League before expanding to Serie A, Bundesliga, La Liga, Ligue 1, and other leagues.

## Initial Candidate Pool

Young senior-level professional outfield players, approximately ages 18–23. Exact age, minute, and league thresholds will be finalized after the data audit.

## Planned Player Output

For each player, the system should eventually provide:

- statistical profile
- strongest characteristics
- percentile rankings
- professional player similarities
- searchable player attributes
- cross-player comparisons

Example concept:

```text
Player X — Central Midfielder

Progressive passing: 91st percentile
Ball carrying:       82nd percentile
Chance creation:     76th percentile
Defensive activity:  61st percentile
Ball retention:      88th percentile

Closest statistical profiles
1. Player A — 91% similarity
2. Player B — 88%
3. Player C — 84%
```

## Project Roadmap

1. **Player Representation** — Can we accurately describe professional players quantitatively?
2. **Player Similarity** — Can we identify genuinely comparable playing profiles?
3. **Player Discovery** — Can we search for players possessing specific combinations of characteristics?
4. **Contextualization** — Can we account for position, team possession, league, age, minutes, tactical environment, and other context?
5. **Development & Potential** — Can historical player trajectories tell us something meaningful about future outcomes?
6. **Club Fit** — Can we characterize what a specific club requires and identify matching players?
7. **Youth Identification** — Can the framework be adapted to less-developed players and limited youth data?
8. **Product** — Can someone use the system effectively through SQL, Python, Tableau/Power BI, and eventually an application?

## Validation Philosophy

The system should be considered useful if it consistently produces football-relevant comparisons between players with similar positions, tactical roles, and playing styles.

A later validation layer will use historical backtesting: for example, evaluating a player using only information available in 2020 and then comparing that profile with how the player developed in subsequent seasons.

Profiling accuracy, similarity accuracy, and future-potential prediction will be treated as separate evaluation problems.

## Known Data Science Challenges

The project will need to address issues such as:

- contextual normalization
- league strength
- age normalization
- sample reliability
- selection bias
- survivorship bias
- data leakage
- tactical and positional role differences

## Current Data Strategy

Current source candidates:

1. **FBref** — main Phase 1 player-season data candidate
2. **Premier League official site** — validation reference
3. **FotMob** — secondary/reference data
4. **StatsBomb Open Data** — event-level experimentation
5. **DataMB + Opta Analyst** — product and methodology references

The current research task is to identify which available metrics meaningfully describe defenders, midfielders, and forwards before committing to a final feature set.

## Planned Technology Stack

- Python
- R
- SQL
- Tableau
- Power BI
- Git / GitHub
- statistical modeling
- machine learning

## Development Philosophy

This repository is intentionally being developed in public as a record of the project's reasoning, experiments, mistakes, revisions, and technical progress.
