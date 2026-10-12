Work Log

This file records the project's development chronologically so that research decisions, scope changes, and reasoning remain visible over time.

2026-09-01 — Project Framing

Initial idea

Build a data-driven soccer player discovery and profiling system that can identify players whose performance characteristics, development trajectory, and playing profile resemble successful players or fit predefined club/role profiles.

The ultimate long-term ambition is to investigate whether young players who may eventually become elite can be identified earlier through data.

Initial player representation concept

Represent each player as a vector in an n-dimensional feature space, potentially including metrics related to progressive passing, progressive carrying, chance creation, defensive actions, pressures, interceptions, passing under pressure, shot creation, and pitch-zone involvement.

Similarity concept

Once players are represented quantitatively, compare profiles using methods such as cosine similarity or Euclidean distance. Any similarity score should be interpretable and accompanied by an explanation of why two players are considered similar.

Talent discovery concept

A future candidate score may incorporate factors such as:

- performance
- age
- development trajectory
- similarity
- league strength
- role fit
- consistency
- minutes
- context

Machine learning may eventually be used to learn such a function, but not before the representation and similarity problems are understood.

Core decision

The project should be framed around the question:

> **Which players should a scout investigate further?**

Early risks identified

- contextual normalization
- league-strength differences
- sample reliability
- selection bias
- survivorship bias
- data leakage

Project charter established

Primary user: club recruitment analyst / sporting director.

Initial candidate pool: young senior-level professional outfield players.

Initial output: key attributes, percentile profiles, professional player comparisons, and searchable/cross-player comparisons.

Roadmap established

1. Player Representation
2. Player Similarity
3. Player Discovery
4. Contextualization
5. Development & Potential
6. Club Fit
7. Youth Identification
8. Product

2026-09-04 — Phase 1 Data Feasibility

Phase 1 question

> **Can we create a meaningful quantitative representation of how a professional soccer player plays?**

Data strategy

Start with the Premier League as a controlled pilot, then expand to Serie A, Bundesliga, La Liga, Ligue 1, and other leagues.

Potential sources identified:

1. FBref — main Phase 1 source candidate
2. Premier League official site — validation
3. FotMob — secondary/reference
4. StatsBomb Open Data — event-level experimentation
5. DataMB + Opta Analyst — product/methodology references
6. Hudl — useful but deferred because the current priority is free data

Current research task

Review available statistics and determine which variables might meaningfully describe:

- defenders and their role variations
- midfielders and their role variations
- forwards and their role variations

The goal is to understand the football meaning of the available metrics before downloading data or building models.

2026-09-05 — Expanded Variable Inventory

Progress

Built broader candidate-variable inventories for four positional families:

- defenders
- midfielders
- forwards
- goalkeepers

The lists currently separate playing-time/context variables, performance variables, additional potentially useful metrics, and per-90 versions of selected statistics.

Examples of newly catalogued candidate metrics include expected goals, expected assisted goals, key passes, passes into the penalty area, through balls, progressive carries, touches by pitch zone, carries into the penalty area, take-ons, ball recoveries, line-breaking passes, dispossessions, duel outcomes, long passing, clearances, physical distance covered, and goalkeeper-specific shot-stopping and sweeping actions.

Emerging design questions

The variable inventory is intentionally broad at this stage. The next step is to organize metrics into football-relevant feature families or subcategories rather than treating each statistic independently.

Important distinctions to address next:

- **context/exposure variables** such as age, matches, starts, minutes, and 90s should not be confused with playing-skill features;
- **per-90 statistics are normalization transformations**, not separate football dimensions;
- raw totals and derived rates may be redundant and should not automatically coexist in the final model;
- a single master feature dictionary may be preferable to permanently duplicating the same variables across positional lists, with role-specific relevance handled later;
- hybrid roles should remain possible, rather than forcing every player into a rigid broad-position feature set.

Next session

Begin converting the raw metric inventory into a structured feature taxonomy, then evaluate which metrics are relevant, redundant, contextual, derived, or unavailable/unconfirmed for each role family.

2026-09-11 to 2026-09-15 — StatsBomb Event-Data Pilot

I explored free StatsBomb Open Data through `statsbombpy` and selected the 2015/16 Premier League metadata entry (`competition_id=2`, `season_id=27`). I used Chelsea vs Arsenal on 2015-09-19 (`match_id=3754217`) as my one-match case study. The match events contain 1,046 Pass events. I exported the event table to CSV and examined its columns, data types, missing values, and pass attributes.

I recognized that a raw event table is more useful as a feature-engineering source than as a direct scouting report. My direction shifted toward converting pass start/end coordinates into useful spatial measurements and eventually displaying them on a pitch. I also decided to keep the original data intact and work with a separate passing DataFrame.

2026-10-12 — Spatial Passing Map Prototype

**Goal:** Turn the Chelsea–Arsenal event data into an individual player pass map and use this as a foundation for an eventual passing network.

**Completed:**
- Created `passingDF` by filtering for `type == "Pass"` and selecting 11 relevant columns (1,046 rows).
- Converted CSV-imported `location` and `pass_end_location` string values into Python coordinate lists with `ast.literal_eval`.
- Extracted `start_x`, `start_y`, `end_x`, and `end_y` numerical columns.
- Calculated `delta_x`, `delta_y`, and Euclidean `calculated_length` using NumPy's `hypot`.
- Compared calculated distance with the original `pass_length`: mean absolute difference `5.193949e-07`, median `3.486958e-07`, maximum `5.491767e-06` across 1,046 passes.
- Interpreted these descriptive statistics as strong numerical agreement with the source measurements, not independent proof of real-world pass-location accuracy.
- Used `mplsoccer` and Matplotlib to draw completed passes separately from other `pass_outcome` values. I kept the original outcome field rather than adding redundant status columns.
- Successfully rendered individual passing maps for Cesc Fàbregas, Mesut Özil, Theo Walcott, and Santi Cazorla. The code is demonstrated across several players, though the plotting blocks are not yet consolidated into one reusable function.
- Added a first-person passing-map explanation and mathematical-validation notes to my research notebook.

**Not yet completed:** A passing network, player-to-player edge table, average pass-origin node positions, jersey number labels, a two-team overlay, interactive filters, an exported enriched passing CSV, or automation across matches. The 380-match listing is metadata; complete match-level event availability should be verified before planning a season-scale run.

**Next session — Passing Network v0.1:**
1. Retrieve the Arsenal lineup through `sb.lineups(match_id=3754217)` and inspect player names and jersey numbers.
2. Filter Arsenal passes with `pass_outcome.isna()` and known `pass_recipient`; consider how to handle special outcomes and set pieces.
3. Create a directed edge table using `groupby(["player", "pass_recipient"]).size()`.
4. Calculate each player's mean pass-start location as an initial network node location (not a measured tracking position).
5. Join jersey numbers and plot weighted connections on an Arsenal pitch with `mplsoccer`.
6. After visual validation, consider splitting by half and making plotting code reusable.

**Methodology questions for later:** StatsBomb coordinates standardize attacking direction, so team overlays require care; player passing networks should account for substitutes and differing playing times; event locations and completed-pass definitions are based on the provider's coding convention.


### 2026-10-12 — End-of-session checkpoint (latest notebook review)

I reviewed my latest local research notebook (`ProjectBlueLock (6).ipynb`) before stopping for the day. The notebook contains the passing-only filtering, coordinate parsing, vector/distance validation, and player-specific pitch plotting experiments. I tested the plotting approach on several players and wrote a first-person explanation of the pipeline.

I have **not yet implemented the passing network** in the notebook. Tomorrow I will start with Arsenal's lineup and jersey numbers, then create passer-to-recipient connection counts and mean pass-origin nodes before plotting the first network. The local notebook is my latest working copy; this work-log entry does not imply that its full `.ipynb` contents have been synced to GitHub.
