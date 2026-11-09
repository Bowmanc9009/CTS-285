# M4 Design Investigation Record

## Product Slice
ST-04: Keyboard-accessible task entry

## Initial Question
What are the exact methods needed in order to make tasks accessible through keyboard?

## Planned Evidence
pseudocode + WCAG mapping

## Evidence Actually Used
- Use-case boundary / actor-goal framing
- Behavior/state flow and two-attempt simulation
- Data-model/schema and Memory Bank constraint stress tests
- Interface/wireframe comparison and state audit
- Design complication and critique

## Findings
### Use-Case Boundary / Question Framing
Learner + typing into the task. How do we make all task able to be accessible only through keyboard

### Behavior / State
What order should a program's steps be ordered in in order to function properly?

### Data / Persistence
how multiple solutions would affect the final product

### Memory Bank Constraint
both business logic and storage help support the flask interface

**Constraint boundary selected:** both

### Interaction
the different answer checker approaches

## Layer Boundary Notes
**Business behavior that should remain outside the interface:**
app routing and extensions

**Data that can be stubbed now:**
have a temporary layer and a permanent layer that saves data later

## New Complication
**Response:** Split the story

splitting may help each to function independently as well as together

## Build-Readiness Decision
**Disposition:** Split / defer part

**Design decision:**
split/ defer

## Revision From Initial Thinking
How carefully I need to think about the order and interactions between each section

## Tradeoff Accepted
separating the uncertainties from what is stable for a more thorough coding experience

## Unresolved Uncertainty
How I will code the attempt try

## Next Question
what do I decide is or is not an uncertain behavior

## Three-Layer Prototype Bridge
Interface: Provide the UI controls, Displayed output, Render data. Business logic: input validation, calculations, workflow. stubbed data layer: data storage/retrieval, CRUD operations for tasks, Stub functionality

## Trace Back to Product Work
able to type entries with only keyboard
