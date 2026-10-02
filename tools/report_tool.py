def create_report(
    goal,
    document_text,
    llm
):

    material = document_text[:30000]

    prompt = f"""
Create a professional structured report.

User goal:
{goal}

Source material:
{material if material else "No uploaded material."}

Use exactly these major sections:

# Report

## Executive Summary

## Key Findings

## Analysis

## Recommendations

## Action Items

The report must be based on the available information.

Do not invent facts.

If source material is missing, clearly state what
information is unavailable.
"""

    return llm(
        "You are NEXUS's professional report generation tool.",
        prompt
    )
