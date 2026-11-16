---
name: create-roadmap
description: Design structured learning roadmaps with stages, lessons, prerequisites, and learning objectives. Use when the user asks to create a roadmap, study plan, curriculum, or systematic learning path for a subject. Save the result to Notion when a suitable connected integration is available and the user requests it.
---

# Create Learning Roadmap

## Goal

Turn a subject into a logically ordered and practical
curriculum that the user can study session by session.

## Inputs

Identify:
- The subject to learn.
- The user's existing knowledge, if available.
- The intended learning outcome.
- Any time, difficulty, or format constraints.

Use reasonable defaults for nonessential missing inputs.

## Workflow

1. Understand the scope of the subject and the user's goal.
2. Research authoritative sources when research tools are available.
3. Identify foundational concepts, prerequisites, and major subfields.
4. Build progressive stages ordered by conceptual dependency.
5. Divide each stage into appropriately sized learning sessions.
6. Assign identifiers such as 1.1, 1.2, 2.1, and 2.2.
7. For each session, specify:
   - Title
   - Learning objectives
   - Concepts and subtopics
   - Prerequisites
   - Practical exercises or applications
8. Review the curriculum for gaps, duplication, and poor sequencing.
9. Present a structured overview.
10. If the user requested persistence, use available Notion tools
    to save the roadmap and establish its associated learning notes.

## Quality requirements

- Teach prerequisites before dependent concepts.
- Allocate more sessions to complex or important concepts.
- Distinguish essential topics from optional advanced topics.
- Make session objectives specific and testable.
- Never invent research sources or claim unavailable tools were used.

## Persistence and failure handling

- Check for an existing matching roadmap before creating duplicates.
- Do not invent Notion database IDs, page IDs, or tool names.
- Only claim that a roadmap or notes store was saved after the
  integration confirms successful creation.
- If persistence is unavailable, return the roadmap in a format
  the user can save manually and explain what remains unsaved.

## Output

Provide:
- Roadmap title and overall learning goal
- Stages and learning sessions
- Estimated scope, when useful
- Prerequisites and suggested starting point
- Notion location or link, if creation succeeded
