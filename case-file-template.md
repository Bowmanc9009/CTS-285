# Analyst's Case File

**System analyzed:** DataMan (Texas Instruments, 1977)
**Feature assigned:** Number Guesser
**Source document:** *The Story of DataMan* — manual transcript

**Charles Bowman:**
**8/30/26**

---

## How to fill this out

Every finding needs evidence. Evidence is an **exact quoted phrase** from the manual plus the **section heading** it came from. Cite sections by name — "Number Guesser (Story)" or "Electro Flash · Number Guesser · Wipe Out (Operating Notes)". Do not cite page numbers; the manual carries two numbering systems that do not agree.

Read **both registers** before you write anything. Part I describes the feature to a child. Part II describes it to an adult. Each contains information the other omits.

If you cannot find evidence for something, do not guess. Put it in Section 8. An unknown you can name is a finding. An assumption you record as fact is an error.

Rows are examples of format, not a quota. Add rows as your evidence requires.

---

## 1. Purpose

Why does this feature exist? What problem does it solve for the user?

| Finding | Evidence (exact quote) | Section |
|---|---|---|
| having fun with math | One thing that annoys AntiMath and makes him green with envy is people having fun with numbers and mathematics! |  A FUN-WITH-NUMBERS GAME! Number Guesser [key: NUMBER GUESSER]|
| sharpening your skills | As you play Number Guesser with your family or friends (or just by yourself), you'll be sharpening your math skills. | A FUN-WITH-NUMBERS GAME! Number Guesser [key: NUMBER GUESSER] |

---

## 2. Users and Roles

Who interacts with this feature? Where a feature involves more than one person, name what each one *does* — the person who sets something up and the person who responds to it are different roles even when they are the same human being.

| Role | What this role does | Evidence (exact quote) | Section |
|---|---|---|---|
| dataman |showing how the game is played and teaching the user  | 'll flash and show you two numbers in my face mask. The secret
number is always somewhere between the two numbers I show you. | HOW TO PLAY |
| user |  | "you enter your guess." |HOW TO PLAY |

---

## 3. Inputs

What information or action enters the system? Include keystrokes, choices, and anything the system refuses to accept.

| Input | Supplied by | Evidence (exact quote) | Section |
|---|---|---|---|
|guesses  | user | You enter your guess. | A FUN-WITH-NUMBERS GAME! Number Guesser [key: NUMBER GUESSER] |

---

## 4. Processing

What does the system do with the input? Include any rule, limit, or constraint you can support.

| Rule or behavior | Evidence (exact quote) | Section |
|hints|As you enter each guess, DataMan provides a hint by displaying two numbers that the
secret number is between.|Number Guesser [key: NUMBER GUESSER] |
| 2 guessing numberse| try to guess a secret number between 9 and 100 that DataMan has selected.  | Number Guesser [key: NUMBER GUESSER] |
| secret number  | press the [NUMBER GUESSER] key. Then, try to guess a secret number between 9 and 100 that DataMan has
selected. As you enter each guess, DataMan provides a hint by displaying two numbers that the
secret number is between.| Number Guesser [key: NUMBER GUESSER] |

---

## 5. Outputs

What information does the system return to the user?

| Output | When it appears | Evidence (exact quote) | Section |
|---|---|---|---|
|  |  |  |  |
| hints after an incorrect answer | helps user get to the right answer without giving them the answer | As you enter each guess, DataMan provides a hint by displaying two numbers that the
secret number is between  | Number Guesser [key: NUMBER GUESSER] |
| secret number | when you turn on the number guesser key | press the [NUMBER GUESSER] key. Then, try to guess a secret number between 9 and 100 that DataMan has
selected. As you enter each guess, DataMan provides a hint by displaying two numbers that the
secret number is between.| Number Guesser [key: NUMBER GUESSER] |
---

## 6. Feedback

How does the system respond to the user's actions? Feedback tells the user how they are doing. An output returns information; feedback comments on it. If you think a single behavior is both, record it once and say why.

| Feedback behavior | What it tells the user | Evidence (exact quote) | Section |
|---|---|---|---|
| total number of guesses | how many guesses it took to get to the answer | DataMan rewards you with a spectacular "light show" and
displays the total number of guesses that were taken. | Number Guesser [key: NUMBER GUESSER] |
|light show for correct answer  | When you finally guess the secret number, I'll show you the number of tries it took, and then a
great light show! | HOW TO PLAY |
---

## 7. Observations and Assumptions

List three statements you were tempted to write as fact but could not fully support. For each, say what evidence you would need.

| Statement | Observation or assumption? | What evidence would settle it? |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

---

## 8. Unknowns and Open Questions

What could not be determined from the manual? For each, state what you looked for and where you looked, so a reader knows the gap is real and not just unsearched.

| Open question | Where I looked | Why the manual does not answer it |
|---|---|---|
| how many attempts until the answer is given to you | operating notes | eventually through enough guesses, the user would get the answer on their own |
|  |  |  |
|  |  |  |

---

## 9. Cross-Register Note

This manual documents the same feature twice. Identify **one** thing your assigned feature's two sections handle differently — something one section states and the other omits, or something the two describe in ways that do not match.

**What differs:**
--- how the rules are explained

**Part I says (quote):**

--- "I'll pick a secret number for you to guess. It will be somewhere between 9 and 100. You enter
your guess. When you do, I'll flash and show you two numbers in my face mask. The secret
number is always somewhere between the two numbers I show you."

**Part II says (quote), or is silent:**

--- "To select this activity, first turn DataMan on with the ON key, and then press the [NUMBER
GUESSER] key. Then, try to guess a secret number between 9 and 100 that DataMan has
selected. As you enter each guess, DataMan provides a hint by displaying two numbers that the
secret number is between."

**Why this matters to an analyst:**

--- this matters because the way the rules are told to you can impact how you view the activity

## Before you submit

- [ ] Every finding has a quoted phrase, not a paraphrase.
- [ ] Every quote names the section it came from.
- [ ] I cited section headings, not page numbers.
- [ ] I read both Part I and Part II before writing.
- [ ] Section 8 is not empty.
- [ ] Nothing in Sections 1-6 is a conclusion I could not support.
