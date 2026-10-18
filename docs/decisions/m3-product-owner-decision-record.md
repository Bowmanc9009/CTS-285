# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-08: Parent progress dashboard (5 pts)

**Why this release slice was defensible:**
highest value with high readiness

**One intentional deferral and why:**
weekly progress summary because summaries could help students and teachers see the user's strong and weak areas

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- ST-08: Parent progress dashboard

### Added after complication
- ST-04: Keyboard-accessible task entry

**What changed and why:**
less point made me have to remove Parent progress dashboard

**Tradeoff accepted:**
ST-04 for ST-08

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.
