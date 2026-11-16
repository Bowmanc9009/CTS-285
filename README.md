# DataMan Text Prototype

This prototype tests the M4 investigation's selected slice, ST-04: keyboard-accessible task entry. It keeps one path small: enter a task using the keyboard, receive a result, and list tasks entered during the current run.

## Run

```sh
python3 app.py
```

Choose `1`, type a title, and press Enter. Choose `2` to verify the task is retained in the current run. A blank title is rejected. All interaction is through terminal text input; no pointer is needed.

## Layer Boundaries

- `app.py` owns prompts, menu choices, and displayed messages.
- `dataman/logic.py` owns the reusable nonblank-title rule and task representation. It accepts a store dependency and does not import the interface or concrete store.
- `dataman/store.py` owns task IDs and in-memory state. Replacing this stub with durable storage should not require changing the entry rule.

## Prototype Evidence

**Provisional acceptance criterion:** Given a user at the task-entry menu, when they enter a nonblank title and submit it, the task is confirmed and appears in the current-run task list. A blank title is rejected and is not stored. Demonstrate this by adding `Practice fractions`, listing tasks, then attempting a blank title.

The focused logic checks are run with `python3 -m unittest discover -s tests`.

## Stubs, Revisions, and Open Questions

- State is deliberately limited to an integer ID and title. The in-memory store resets on exit; accounts, persistence, task editing, completion, and database behavior are not implemented.
- M4 names ST-04 as keyboard-accessible task entry but does not define acceptance criteria. The criterion above is provisional and makes successful submission, visible confirmation, retained current-run state, and blank rejection observable.
- **Revision from prototype testing:** M4 did not say what blank submission should do. Exercising the entry path showed this needed an explicit rule, so blank titles are now rejected without changing stored state; the provisional acceptance criterion includes that behavior.
- The M4 record's task-entry slice comes from the StudyTrack release decision, while the DataMan requirements/backlog in this repository focus on math-answer feedback and do not define a task entity. Confirm whether ST-04 is intended for DataMan before carrying its model into Module 5.
- Terminal interaction confirms that this path needs no pointer and exercises the input/state flow; it does not test focus order, semantic labels, screen-reader announcements, or keyboard behavior in a graphical interface. Those remain unresolved for a real UI.
- The investigation says temporary and permanent data layers may both be needed. This run confirmed the temporary boundary is sufficient for the slice, but persistence duration and identity remain undecided.