def generate_quiz(
    goal,
    document_text,
    llm
):

    material = document_text[:30000]

    prompt = f"""
Generate a 10-question multiple-choice quiz.

User goal:
{goal}

Study material:
{material if material else "No uploaded material."}

Requirements:

- Exactly 10 questions.
- Each question must have 4 options.
- Clearly identify the correct answer.
- Give a short explanation.
- Questions should be based on the uploaded material
  when material is available.
- Do not invent document-specific facts that are not present.

Use this format:

# Practice Quiz

## Question 1
Question text

A. Option
B. Option
C. Option
D. Option

**Correct Answer:** A

**Explanation:** Short explanation.
"""

    return llm(
        "You are NEXUS's quiz generation tool.",
        prompt
    )
