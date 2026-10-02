def create_study_plan(
    goal,
    document_text,
    llm
):

    material = document_text[:30000]

    prompt = f"""
Create a practical study plan.

User goal:
{goal}

Study material:
{material if material else "No uploaded material."}

Create a structured response containing:

# Study Plan

## Important Topics

List the most important topics.

## Priorities

Classify topics as:
- High Priority
- Medium Priority
- Low Priority

## 7-Day Schedule

Create a generic 7-day plan.

Do not invent a real calendar date.

Include:
- Day 1
- Day 2
- Day 3
- Day 4
- Day 5
- Day 6
- Day 7

## Revision Strategy

Explain how the student should revise.

## Daily Tasks

Give concrete tasks for each day.

If there is not enough information to determine exact
study hours, provide flexible recommendations instead.
"""

    return llm(
        "You are NEXUS's study planning tool.",
        prompt
    )
