# Project Charter v0.2

## Problem

Soccer clubs have limited scouting resources and must evaluate large numbers of potential players across leagues, teams, positions, and competitive environments.

## Primary User

Club recruitment analysts and sporting directors.

## Core Decision

Determine which players deserve further scouting based on statistical characteristics and desired player profiles.

## Initial Candidate Pool

Young senior-level professional outfield players, with exact age and league thresholds to be determined after investigating available data.

A working initial range is approximately 18–23 years old.

## Initial System Output

For each player:

- statistical profile
- strongest characteristics
- percentile rankings
- professional player similarities
- searchable player attributes
- cross-player comparison

## Long-Term Goal

Expand the system toward identifying undervalued and emerging talent while incorporating:

- development trajectory
- tactical fit
- league strength
- age
- physical/tracking information
- eventually youth players

## Core Modeling Principle

The system should help answer:

> **Which players should a scout investigate further?**

It should not be framed initially as an automatic signing decision or as a definitive predictor of future elite status.

## Role-Aware Comparison

Player similarity should respect football roles, not only broad position labels.

Examples include:

- forwards: winger, striker, false 9, and related variations
- midfielders: 6, 8, 10, holding midfielder, ball-carrying midfielder, box-to-box midfielder, and related variations
- defenders: left back, right back, centre back, and related variations

The long-term system should distinguish between positional family and tactical archetype.

## Validation Philosophy

The system should be considered effective if it consistently produces football-relevant comparisons between players with similar positions, tactical roles, and playing styles.

A second major validation method will be historical backtesting. For example:

1. take only information available for a player in 2020
2. generate the player's profile and comparison set
3. freeze the model output
4. compare the result with how the player developed in later seasons

Profiling accuracy, similarity accuracy, and future-potential prediction are separate evaluation problems and should not be conflated.

## Known Data Science Risks

- contextual normalization
- league strength differences
- age normalization
- sample reliability
- selection bias
- survivorship bias
- data leakage
- tactical context
- position and role ambiguity
