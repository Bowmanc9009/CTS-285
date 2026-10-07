# DataMan Requirements Register

> Replace all bracketed prompts with your own project evidence and requirements. Delete the prompts before submitting.

## Project Context

[Students, Parents, and Teachers should be able to use a new, modernized version of dataman. Dataman has many separate functions, but its main goal is to be a fun and useful tool to help kids learn math.]

## Evidence Notes

Use at least four concise evidence statements. Label the source of each.

- **E-01 — Source:** [Simulation]  
  **Evidence:** [Stakeholders say modern means the experience should work reliably in a browser, be understandable without a printed manual, and avoid making the learner navigate unnecessary screens. They do not specify a visual style or framework.]

- **E-02 — Source:** [simulation]  
  **Evidence:** [Teachers report that students may pause practice and return later. They want a learner’s saved practice state to remain available after leaving and returning to the application.]

- **E-03 — Source:** [simulation]  
  **Evidence:** [Stakeholders identify immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as central to the original experience.]

- **E-04 — Source:** [simulation]  
  **Evidence:** [Adults want to understand what the learner practiced and whether progress is occurring]

[Add additional evidence notes if needed.]

## Functional Requirements

Write at least four functional requirements. Each requirement should describe a capability or behavior the system must provide.

### FR-01
**Requirement:** The system must [Responsive and reliable].  
**Source/Rationale:** [Stakeholders identify immediate answer feedback]

### FR-02
**Requirement:** The system must [have authentication for sessions].  
**Source/Rationale:** [teachers want students to be able to save their work through authenticated sessions]

### FR-03
**Requirement:** The system must [able to run the multiple functions of the original dataman].  
**Source/Rationale:** [this project is a modernization of Dataman, so this program should be able to the many detailed activities the original Dataman did]

### FR-04
**Requirement:** The system must [check answers for students without immediately telling them the right answer].  
**Source/Rationale:** [activities such as number guesser and answer checker give feedback without giving them the answers. this allows the user to learn instead of using it like a cheatsheet]

[Add additional functional requirements if needed.]

## Non-Functional Requirements

Write at least three non-functional requirements. Each requirement should describe a measurable quality, constraint, or condition the system must satisfy.

### NFR-01
**Requirement:** The system must [be reliable and consistant ].  
**Source/Rationale:** [In general, users of all kinds want consistancy and reliability in the tools they use. a messy or buggy program will impede success.]

### NFR-02
**Requirement:** The system must [have easily accessible feedback].  
**Source/Rationale:** [dataman is supposed ot help you practice math so you need the feedback given should be easily decipherable and accessible]

### NFR-03
**Requirement:** The system must [have each dataman minigame be separately accessible].  
**Source/Rationale:** [users would want to have each game they want to play be readily available and accessible]

[Add additional non-functional requirements if needed.]

## Open Questions / Assumptions

Do not turn an unsupported idea into a confirmed requirement. Record unresolved items here until evidence supports a decision.

- **Q-01:** [What systems need to be used]
- **Q-02:** [what a readible system for parents and teachers looks like]

[Add or remove items as appropriate.]

## Final Quality Check

Before submitting, confirm that each requirement is:

- [ ] Clear enough for another team member to interpret consistently.
- [ ] Supported by evidence, a stakeholder need, or a confirmed project constraint.
- [ ] Testable or verifiable later.
- [ ] Solution-neutral enough for this stage of the project.
- [ ] Focused on one main capability or quality.
- [ ] Classified correctly as functional or non-functional.

Also confirm:

- [ ] At least four functional requirements are included.
- [ ] At least three non-functional requirements are included.
- [ ] Every confirmed requirement has a source/rationale.
- [ ] Open questions and assumptions are separated from confirmed requirements.
- [ ] The simulation decision record is saved at `docs/decisions/m2-elicitation-decision-record.md`.
- [ ] This file is saved as `docs/requirements.md`, committed, and synced to GitHub.