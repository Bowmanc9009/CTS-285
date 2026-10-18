# DataMan Product Backlog

## Sources

This backlog uses these files from my repository:

- `doc/requirements.md`
- `doc/docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`

The version of the requirements was refined during module 2 and then checked against the triage and release-planning decisions before finalizing this backlog.

## Priority Order

1. US-01
2. US-02
3. US-03
4. US-04

## Stories

### US-01 — Immediate Answer Feedback

**Requirement ID:** FR-01, FR-04, NFR-02

**User Story:** As a learner, I want immediate feedback on each answer so that I can correct my thinking while I am practicing.

**Acceptance Criteria:**

- Given a learner submits an answer, when the answer is checked, then the system shows a clear result without immediately revealing the exact correct answer.
- Given a learner answers incorrectly, when feedback appears, then the learner can see whether the answer was too high, too low, or otherwise incorrect.
- Given the learner is practicing, when feedback is displayed, then it is visible on the same screen and easy to interpret.

**Relative Effort:** S — This is a small, core interaction and it is simpler than session persistence or reporting work.

**Dependency / Constraint:** None

**Priority:** 1

**Readiness:** Move Forward

**Priority Rationale:** This item has the highest value because immediate feedback is required for a usable first release, and it combines high stakeholder value with low effort and low risk.

---

### US-02 — Retry After Incorrect Response

**Requirement ID:** FR-04, NFR-02

**User Story:** As a learner, I want to retry after a missed answer so that I can practice the same skill repeatedly and improve.

**Acceptance Criteria:**

- Given a learner answers incorrectly, when the system checks the answer, then the learner is allowed to try the exercise again without leaving the current activity.
- Given a learner submits a new attempt, when the system evaluates it, then the learner sees updated feedback for the most recent response.
- Given a learner completes multiple attempts, when the activity is still in progress, then the learner can clearly understand their current status.

**Relative Effort:** S — This is still a small feature compared with broader session and summary work, but it exercises the same high-value learning loop.

**Dependency / Constraint:** US-01

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** This is a direct extension of the answer-checking flow and has high value with low effort, which makes it a strong second release item before more uncertain work begins.

---

### US-03 — Teacher and Parent Progress Summary

**Requirement ID:** NFR-02, NFR-03

**User Story:** As a parent or teacher, I want a summary of what a learner practiced and how they are progressing so that I can support learning and identify gaps.

**Acceptance Criteria:**

- Given a learner has completed practice, when the summary is viewed, then it shows the activity or skill the learner practiced.
- Given a learner has multiple attempts, when the summary is reviewed, then it includes evidence of recent progress.
- Given a parent or teacher opens the summary, when they view it, then the information is readable without extra training.

**Relative Effort:** M — This is larger than the feedback loop because it depends on collecting and summarizing learner data, but it remains smaller than a full session-persistence design.

**Dependency / Constraint:** US-01, US-02

**Priority:** 3

**Readiness:** Refine

**Priority Rationale:** The value is meaningful for supporting adults, but the reporting model and data structure still need more definition, so it should be refined before commitment.

---

### US-04 — Preserve Learner Progress Between Sessions

**Requirement ID:** FR-02, NFR-01

**User Story:** As a learner, I want my practice state to be available when I return later so that I can continue without losing progress.

**Acceptance Criteria:**

- Given a learner leaves the application, when they return later, then their saved practice state is still available.
- Given a learner starts a session, when the system loads saved progress, then the learner resumes from the previous state instead of starting over.
- Given a learner resumes a saved session, when the app restores state, then the learner can continue without obvious errors or data loss.

**Relative Effort:** L — This is a larger item because it depends on account or session design decisions that are still uncertain and more complex than the core learning loop.

**Dependency / Constraint:** Account or session approach is not yet ready; identity and persistence decisions must be resolved first.

**Priority:** 4

**Readiness:** Defer

**Priority Rationale:** The value is high, but the dependency uncertainty and implementation size make this a poor fit for the first release until the session model is clearly defined.

---

## Open Questions Carried Forward

- **Q-01:** What systems need to be used? This question affects the design of persistent learner sessions and any teacher or parent reporting model, and no story is ready to commit until the platform and identity approach is defined.
- **Q-02:** What does a readable system for parents and teachers look like? This affects the progress-summary story because the reporting structure and audience needs are still being clarified.

## Revisions After Triage and Release Planning

- US-04 — Deferred from Refine to Defer because the account/session approach was not ready, and the backlog triage record explicitly called out the uncertainty around persistent identity.
- US-03 — Kept in Refine status because the value remains meaningful, but the data model and reporting design still need clarification before the item is ready for a release slice.
- US-01 and US-02 — Kept as Move Forward because the instructor stakeholder identified immediate feedback and repeated attempts as required for the first usable release.

## Before You Submit

- [x] The file path is exactly `docs/product-backlog.md`.
- [x] All bracketed prompts and unused story blocks are removed.
- [x] Every story has all eight required fields: Story ID, Requirement ID, User Story, Acceptance Criteria, Relative Effort, Dependency / Constraint, Priority, Priority Rationale.
- [x] Every Requirement ID exists in `doc/requirements.md`.
- [x] Each acceptance criterion states a result another person can observe and check.
- [x] The story blocks follow the Priority Order list.
- [x] Large or uncertain stories are marked Refine or Defer, not hidden as Move Forward.
- [x] No story or criterion names a framework, database, or screen layout, unless a requirement makes it a constraint.
- [x] The file renders correctly on GitHub.
- [x] The change is committed with a message that describes it.
