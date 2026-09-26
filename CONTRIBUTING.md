# 📜 Contribution Rules & Conventions

This file defines **all the rules** for this repository.
Whether I'm writing myself or asking for help — everything must follow this guide.

> **Consistency over frequency.** There's no pressure to write every day.
> Write whenever you learn something worth keeping — even once a week is valuable.

---

## 1. Language

- **All content must be written in English** — this is intentional, to practice technical writing.
- For **difficult or ambiguous terms**, add a Vietnamese translation on the next line using this format:

  ```markdown
  ## Closure
  > 🇻🇳 *Hàm có thể truy cập biến của phạm vi bên ngoài dù phạm vi đó đã kết thúc.*

  A closure is a function that retains access to its lexical scope...
  ```

- Keep language **simple and clear** — write as if explaining to a junior developer.

---

## 2. Folder Structure

```
my-dev-notes/
├── topics/                  # Tech-specific knowledge
│   ├── <topic-name>/
│   │   ├── README.md        # REQUIRED: index/overview of this topic
│   │   └── <subtopic>.md    # One file per focused subtopic
│   └── README.md            # Index of all topics
│
└── fundamentals/            # Language-agnostic CS concepts
    ├── algorithms/
    │   ├── README.md
    │   └── <algorithm>.md   # e.g., binary-search.md, bubble-sort.md
    ├── data-structures/
    │   ├── README.md
    │   └── <structure>.md   # e.g., linked-list.md, hash-table.md
    ├── networking/
    │   ├── README.md
    │   └── <concept>.md
    ├── system-design/
    │   ├── README.md
    │   └── <concept>.md
    └── README.md            # Index of all fundamentals categories
```

### `topics/` folder
- For notes about a **specific technology, tool, or framework** (e.g., React, Docker, PostgreSQL).
- Each technology gets its **own subfolder**.
- Each subfolder **must** have a `README.md` as an overview/index.
- Split into multiple `.md` files when a topic grows large (e.g., `hooks.md`, `state-management.md`).

### `fundamentals/` folder
- For **language-agnostic** Computer Science knowledge that applies regardless of tech stack.
- Organized into **category subfolders** (algorithms, data-structures, networking, system-design, security...).
- Each subfolder has its own `README.md` index.
- Each concept within a subfolder is a **single `.md` file**.
- Create a new subfolder when a category has (or will have) more than one note.

---

## 3. File Naming

| Rule | Example |
|------|---------|
| All **lowercase** | ✅ `event-loop.md` ❌ `EventLoop.md` |
| Use **hyphens** (not underscores or spaces) | ✅ `data-types.md` ❌ `data_types.md` |
| Name should reflect the **content**, not the date | ✅ `closures.md` ❌ `2026-09-26.md` |
| Keep names **short but descriptive** | ✅ `async-await.md` ❌ `notes-about-async-await-in-js.md` |

---

## 4. File Content Structure

Every `.md` note file should follow this template, using a **"Why-first"** approach:

```markdown
# <Topic Title>
> 🇻🇳 *(Vietnamese translation if needed)*

## Why does it exist?
<!--
  Start here. Answer these questions:
  - What problem existed BEFORE this was created?
  - What "pain" does it solve for developers?
  - Why was it invented / what gap did it fill?
  Think: "Without this, developers had to deal with X..."
-->

## What is it?
<!-- Now define it clearly in your own words, given the context above. -->

## How it works
<!-- Explain the mechanism, the internals, the mental model. -->

## Example
<!-- Code block or real-world analogy that makes it concrete. -->

## Key Takeaways
<!-- 3-5 bullet points: the most important things to remember. -->

## References
<!-- Links to articles, docs, or videos that helped you understand this. -->
```

> **Note:** Not every section is mandatory. Skip sections that don't apply,
> but **always include at least `Why does it exist?` and `Example`** — these two anchor the whole note.

---

## 5. README.md inside each topic folder

Every topic folder must have a `README.md` that acts as a **table of contents**:

```markdown
# <Technology Name>

> Brief one-line description of what this technology is.

## Notes

| File | Description |
|------|-------------|
| [closures.md](./closures.md) | How closures work and why they matter |
| [event-loop.md](./event-loop.md) | Understanding JS single-threaded async model |
```

Update this file every time you add a new note to the folder.

---

## 6. Commit Message Format

Git commit history is the **daily learning log** of this repository.
A well-written commit = a record of what was learned on that day.

### Format

```
<type>(<topic>): <short description — written like a title>

- Key point 1
- Key point 2
- Key point 3
- Ref: https://link-to-source.com
```

### Types

| Type | When to use |
|------|-------------|
| `note` | Adding a new note or concept |
| `update` | Expanding or correcting an existing note |
| `struct` | Restructuring folders, renaming files |
| `fix` | Fixing a factual error or typo in a note |
| `chore` | Updating README, CONTRIBUTING, or other meta files |

### Rules for the subject line
- Use **imperative mood**: `note(react): understand useEffect cleanup` ✅ (not "noted" or "noting")
- Keep it **under 72 characters**
- The `<topic>` should match the **folder name** (e.g., `react`, `docker`, `networking`)
- **Do NOT include a date** in the subject — Git timestamps it automatically

### Examples

```
note(javascript): understand closure and lexical scope

- A closure retains access to its outer scope even after the outer function returns
- Variables are captured by reference, not by value
- Common pattern: factory functions, data encapsulation, memoization
- Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
```

```
note(networking): how DNS resolution works

- DNS translates human-readable domain names to IP addresses
- Resolution order: browser cache → OS cache → Resolver → Root → TLD → Authoritative
- TTL controls how long a record is cached
- Ref: https://howdns.works
```

```
update(react): add more examples to useCallback note

- Added comparison between useMemo and useCallback
- Clarified when NOT to use useCallback (premature optimization)
```

```
struct: reorganize docker folder into subfiles

- Split docker.md into: basics.md, networking.md, compose.md
- Updated topics/docker/README.md index
```

---

## 7. Quick Checklist before committing

- [ ] Content is written in **English**
- [ ] Hard terms have a `> 🇻🇳` translation if needed
- [ ] File is named with **lowercase and hyphens**
- [ ] File follows the **content structure template**
- [ ] The folder's **`README.md` index is updated**
- [ ] Commit message follows the **correct format**
