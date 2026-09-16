# Slide Editing Spec

## Goal

Improve an existing Bento Slides presentation that introduces an academic paper.

- Presentation length: 15-20 minutes.
- Target: about 10 main slides.
- Audience: a classroom, so text must be large and easy to read.
- Output: an editable `.bento.html` file.

## Sources

Use Notion MCP to read the presentation-planning page and paper-review page.

```text
Presentation page: https://app.notion.com/p/Presentation-Prep-3d076c60b241808e9ff4c5a5d8afa6a4?source=copy_link
Paper review page: https://app.notion.com/p/Paper-Review-3d776c60b24180c89f73fadbbc71068c?source=copy_link
```

Use these pages to understand the requested structure, content, examples, results, and limitations. Check the original paper when a claim or number needs verification.

## Editing requirements

- Edit the existing deck instead of rebuilding it from scratch.
- Preserve the official Bento editor and the existing visual style.
- Keep approximately one main idea per slide.
- Shorten crowded text instead of reducing the font size.
- Use diagrams, charts, or tables when they communicate better than paragraphs.
- Keep the presenter name and other placeholders editable.
- Add speaker notes when useful.

## Animation

Use Bento animations only when they help explain the content:

- `morph` for related slides or changing diagrams;
- `fade-up` for sequential steps;
- `countUp` for important results;
- interactive states for optional details.

Avoid excessive or distracting animation.

## Technical requirements

- Keep the official Bento HTML application shell unchanged.
- Edit only the JSON inside the `#bento-doc` script block.
- Do not replace Bento with a custom HTML slideshow.
- Keep element IDs stable when possible so morph transitions continue to work.
- Do not include collaboration keys or other secrets.

## Done when

- The deck opens in the full Bento editor.
- Existing elements remain editable.
- The presentation fits approximately 15-20 minutes.
- Text is readable and nothing overlaps or overflows.
- Animations work in slideshow mode.
- `window.bento.validate()` reports no errors or warnings.
