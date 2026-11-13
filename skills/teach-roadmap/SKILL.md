
---
name: teach-lesson
description: Teach or resume a specific session from an existing learning roadmap. Use when the user requests a numbered lesson such as 2.3, asks to continue a roadmap, or wants to study the next session. Retrieve the session outline and relevant past learning notes when connected sources are available.
---

# Teach Learning Session

## Goal

Deliver a clear, accurate, practical lesson that fits the
user's roadmap and builds on previous learning.

## Inputs

Identify:
- The roadmap.
- The requested session or next unfinished session.
- The official session objectives and topics.
- Relevant prior lessons, notes, and learning progress.

## Workflow

1. Resolve the requested roadmap and session.
2. Retrieve the session definition from the connected source.
3. Retrieve relevant past learning notes when available.
4. Identify prerequisites and learning objectives.
5. Explain the topic from foundational ideas to deeper concepts.
6. Use practical examples suited to the subject.
7. Explain how the new concepts connect to previous lessons.
8. Include exercises or questions to check understanding.
9. Summarize the most important concepts.
10. When authorized and supported, append a factual
    session summary to the roadmap's learning notes.

## Teaching requirements

- Explain why concepts matter, not merely their definitions.
- Use examples, analogies, and practical applications.
- Distinguish scientific facts from interpretations or speculation.
- Adjust depth based on available evidence of prior knowledge.
- Do not claim the user has mastered a concept without evidence.
- Do not skip essential material just to make the lesson shorter.

## Missing context and failure handling

- If multiple roadmaps match, ask which one the user wants.
- If the requested session cannot be located, do not invent
  its official outline or pretend it was retrieved.
- If past notes are unavailable, explain that limitation and
  continue from the session outline when possible.
- Never invent previous lesson outcomes or progress.
- Never claim that notes were saved unless confirmed.
- Do not overwrite existing notes when an append is intended.

## Output

Provide:
- Lesson title and objectives
- Prerequisite recap
- Detailed explanation with examples
- Practical exercises
- Knowledge-check questions
- Summary and connection to the next lesson
- Persistence status, when notes were saved or attempted
