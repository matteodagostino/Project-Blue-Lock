# Feature Notes

## Phase 1 Research Question

> **Can we create a meaningful quantitative representation of how a professional soccer player plays?**

The immediate task is to identify which available variables might meaningfully describe different positional and tactical roles before selecting a final feature set.

## Player Representation Concept

Represent each player as a vector:

\[
X = [x_1, x_2, x_3, \ldots, x_n]
\]

where features may capture dimensions such as:

- ball progression
- chance creation
- defensive contribution
- passing
- possession
- ball carrying
- shot creation
- touches in different zones
- ball recoveries
- pressures
- interceptions

The exact feature set is intentionally undecided at this stage.

## Position Research

### Defenders

Research prompt:

> Which available variables actually tell us something meaningful about how a defender plays?

Potential sub-roles to consider later include:

- centre back
- ball-playing centre back
- stopper
- left back
- right back
- attacking fullback
- defensive fullback
- inverted fullback

### Midfielders

Research prompt:

> Which available variables actually tell us something meaningful about how a midfielder plays?

Potential sub-roles to consider later include:

- 6
- 8
- 10
- holding midfielder
- box-to-box midfielder
- ball-carrying midfielder
- deep-lying playmaker
- advanced playmaker

### Forwards

Research prompt:

> Which available variables actually tell us something meaningful about how a forward plays?

Potential sub-roles to consider later include:

- striker
- winger
- inside forward
- false 9
- target forward
- wide forward

## Important Design Principle

Broad position labels alone are not enough. A future similarity model should be able to distinguish tactical role and playing style within positional families.

## Candidate Feature Families

These are working conceptual buckets, not final engineered features:

- ball progression
- creativity / chance creation
- ball carrying
- defensive activity
- ball retention / security
- goal threat
- passing profile
- duel profile
- spatial involvement

Each bucket will need to be justified with raw metrics and tested for redundancy, scaling, context dependence, and interpretability.
