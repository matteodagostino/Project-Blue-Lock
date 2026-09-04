# Work Log

This file records the project's development chronologically so that research decisions, scope changes, and reasoning remain visible over time.

## 2026-09-01 — Project Framing

### Initial idea

Build a data-driven soccer player discovery and profiling system that can identify players whose performance characteristics, development trajectory, and playing profile resemble successful players or fit predefined club/role profiles.

The ultimate long-term ambition is to investigate whether young players who may eventually become elite can be identified earlier through data.

### Initial player representation concept

Represent each player as a vector in an n-dimensional feature space, potentially including metrics related to progressive passing, progressive carrying, chance creation, defensive actions, pressures, interceptions, passing under pressure, shot creation, and pitch-zone involvement.

### Similarity concept

Once players are represented quantitatively, compare profiles using methods such as cosine similarity or Euclidean distance. Any similarity score should be interpretable and accompanied by an explanation of why two players are considered similar.

### Talent discovery concept

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

### Core decision

The project should be framed around the question:

> **Which players should a scout investigate further?**

### Early risks identified

- contextual normalization
- league-strength differences
- sample reliability
- selection bias
- survivorship bias
- data leakage

### Project charter established

Primary user: club recruitment analyst / sporting director.

Initial candidate pool: young senior-level professional outfield players.

Initial output: key attributes, percentile profiles, professional player comparisons, and searchable/cross-player comparisons.

### Roadmap established

1. Player Representation
2. Player Similarity
3. Player Discovery
4. Contextualization
5. Development & Potential
6. Club Fit
7. Youth Identification
8. Product

## 2026-09-04 — Phase 1 Data Feasibility

### Phase 1 question

> **Can we create a meaningful quantitative representation of how a professional soccer player plays?**

### Data strategy

Start with the Premier League as a controlled pilot, then expand to Serie A, Bundesliga, La Liga, Ligue 1, and other leagues.

Potential sources identified:

1. FBref — main Phase 1 source candidate
2. Premier League official site — validation
3. FotMob — secondary/reference
4. StatsBomb Open Data — event-level experimentation
5. DataMB + Opta Analyst — product/methodology references
6. Hudl — useful but deferred because the current priority is free data

### Current research task

Review available statistics and determine which variables might meaningfully describe:

- defenders and their role variations
- midfielders and their role variations
- forwards and their role variations

The goal is to understand the football meaning of the available metrics before downloading data or building models.
