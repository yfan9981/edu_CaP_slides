# Code as Policies Slides

This repository contains a self-contained [Bento Slides](https://bento.page) presentation about *Code as Policies*. The deck is designed for a 15-20 minute classroom presentation and remains editable as structured JSON inside a single HTML file.

## Quick Start

No package installation or build step is required.

1. Clone the repository and open it in VS Code.
2. Open [slides/CaP_AI_Working.bento.html](slides/CaP_AI_Working.bento.html) in Safari 16.4+, Firefox 113+, Chrome, or Edge.
3. Use the Bento editor to inspect or edit the deck. Use presentation mode to review transitions, animations, and speaker notes.

The working deck is self-contained, so it can be opened directly from disk. A local web server is optional, not required.

## Repository Map

| File | Purpose |
| --- | --- |
| [slides/CaP_AI_Working.bento.html](slides/CaP_AI_Working.bento.html) | Current editable and shareable working deck. |
| [slides/CaP_Original.bento.html](slides/CaP_Original.bento.html) | Original/source deck. Treat it as an archive and do not edit it casually. |
| [sanitize_bento.py](sanitize_bento.py) | Removes the top-level `collab` object from the original and writes the working copy. |
| [SPEC.md](SPEC.md) | Presentation goals and editing requirements. |
| [AGENTS.md](AGENTS.md) | Bento authoring, validation, layout, and security reference. |

## Editing Rules

The document source of truth is the JSON inside the `script` block with `id="bento-doc"`.

- Edit only the JSON inside `#bento-doc`; leave the Bento HTML shell and compressed runtime unchanged.
- Preserve `docId` and existing slide and element IDs whenever possible. Stable IDs keep morph transitions working.
- Escape `<` as `\u003c` when writing HTML-embedded JSON so the JSON cannot terminate the script block.
- Keep text readable for a classroom. Prefer shortening crowded copy or using a chart/table instead of shrinking fonts.
- Preserve the existing visual language unless a change is intentional and agreed upon.
- When deleting content, remove its JSON object instead of hiding it with opacity, off-canvas positioning, or a cover shape.
- Keep changes focused. Report changed, added, and deleted slide or element IDs in the Pull Request description.

## Validate Before Sharing

Open the working deck in a browser and run this in the developer console:

```js
const result = window.bento.validate()
result.findings.filter((finding) => finding.severity !== "info")
```

Resolve errors and warnings before opening a Pull Request. Then page through every slide manually and check:

- text overflow and accidental overlap;
- chart and table rendering;
- morph transitions and other animations in presentation mode;
- speaker notes and links;
- editability of existing elements.

Validation is useful, but it does not replace looking at the rendered deck.

## Collaboration Workflow

Use a feature branch for each focused change:

```bash
git switch -c update/<short-description>
# edit and validate the deck
git diff --check
git add README.md slides/CaP_AI_Working.bento.html
git commit -m "Describe the change"
git push -u origin update/<short-description>
```

Open a Pull Request with:

- a short summary of the presentation change;
- the affected slide IDs and element IDs;
- the output or result of `window.bento.validate()`;
- any visual review notes or known follow-up work.

Because a `.bento.html` file contains a large embedded runtime, resolve merge conflicts carefully. Keep the runtime and unrelated JSON unchanged, and prefer one person editing a given slide at a time.

## Security: Remove Collaboration Keys

Do not publish a deck containing collaboration credentials. In particular, never commit or paste a deck containing `collab`, `ownerPriv`, `writerPriv`, or `invite` values into GitHub issues, Pull Requests, chat, or AI tools.

The existing sanitizer reads `slides/CaP_Original.bento.html`, removes its top-level `collab` object, and overwrites `slides/CaP_AI_Working.bento.html`:

```bash
python3 sanitize_bento.py
```

Review the command before running it: it uses fixed input/output paths and replaces the working copy. Afterward, verify that the working deck contains no collaboration object:

```bash
rg -n '"(collab|ownerPriv|writerPriv|invite)"' slides/CaP_AI_Working.bento.html
```

An empty result is expected. Removing keys after a live deck has already been shared does not revoke the old room; use Bento's key rotation controls if that has happened.

## Contribution Checklist

- [ ] Work on a feature branch.
- [ ] Edit the intended working deck, not the original archive.
- [ ] Preserve `docId`, stable IDs, and the Bento shell.
- [ ] Run `window.bento.validate()` and resolve non-info findings.
- [ ] Review every slide in the browser.
- [ ] Run `git diff --check`.
- [ ] Confirm no collaboration keys are present before pushing.
- [ ] Describe the affected IDs in the Pull Request.

## Troubleshooting

**The deck does not open:** use a current browser, and make sure you opened the `.bento.html` file rather than the Markdown documentation.

**The editor shows unexpected content:** confirm that you are using `CaP_AI_Working.bento.html`. Keep `CaP_Original.bento.html` as the source/archive copy.

**Validation reports a broken link or asset:** check the referenced slide ID or asset key in the same `#bento-doc` JSON block.

**A merge conflict affects the deck:** preserve the HTML shell and runtime, resolve the JSON deliberately, then reopen the file and validate the complete deck before committing.
