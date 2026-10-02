import json
from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL
from tools.document_tool import extract_document
from tools.study_tool import create_study_plan
from tools.quiz_tool import generate_quiz
from tools.report_tool import create_report


class NexusAgent:

    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing from Streamlit Secrets.")

        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL

    def _llm(self, system_prompt, user_prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    def _make_plan(self, goal, document_text=""):

        prompt = f"""
You are the planning brain of an autonomous AI agent.

User goal:
{goal}

A document was uploaded: {"Yes" if document_text else "No"}

Choose the tools required to complete the goal.

Available tools:
- document
- study
- quiz
- report

Return ONLY valid JSON:

{{
    "plan": [
        "step 1",
        "step 2"
    ],
    "tools": [
        "tool_name"
    ]
}}

Do not write anything outside the JSON.
"""

        try:
            result = self._llm(
                "You are a precise AI agent planner.",
                prompt
            )

            start = result.find("{")
            end = result.rfind("}") + 1

            if start == -1 or end == 0:
                raise ValueError("Invalid planner response.")

            data = json.loads(result[start:end])

            plan = data.get("plan", [])
            tools = data.get("tools", [])

            allowed_tools = [
                "document",
                "study",
                "quiz",
                "report"
            ]

            tools = [
                tool for tool in tools
                if tool in allowed_tools
            ]

            if not tools:
                tools = ["report"]

            if not plan:
                plan = ["Understand the user goal", "Execute required tools", "Generate final result"]

            return plan, tools

        except Exception:

            goal_lower = goal.lower()

            tools = []

            if document_text:
                tools.append("document")

            if any(word in goal_lower for word in [
                "study",
                "learn",
                "schedule",
                "plan"
            ]):
                tools.append("study")

            if any(word in goal_lower for word in [
                "quiz",
                "mcq",
                "questions",
                "test"
            ]):
                tools.append("quiz")

            if any(word in goal_lower for word in [
                "report",
                "analysis",
                "analyze",
                "summary",
                "summarize"
            ]):
                tools.append("report")

            if not tools:
                tools = ["report"]

            plan = [
                "Understand the user's goal",
                "Select appropriate AI tools",
                "Execute the selected tools",
                "Synthesize the final result"
            ]

            return plan, tools

    def run(self, goal, uploaded_file=None):

        execution = []

        document_text = ""

        # STEP 1: Document extraction
        if uploaded_file is not None:

            execution.append("Reading uploaded document...")

            try:
                document_text = extract_document(uploaded_file)

                execution.append(
                    "Document successfully processed."
                )

            except Exception as e:
                execution.append(
                    "Document processing failed."
                )

        # STEP 2: Planning
        execution.append("AI agent is creating a plan...")

        plan, tools = self._make_plan(
            goal,
            document_text
        )

        execution.append(
            "AI plan created successfully."
        )

        # STEP 3: Tool execution
        tool_results = {}

        for tool in tools:

            execution.append(
                f"Executing {tool} tool..."
            )

            try:

                if tool == "document":

                    tool_results["document"] = {
                        "status": "success",
                        "content": document_text[:20000]
                    }

                elif tool == "study":

                    tool_results["study"] = create_study_plan(
                        goal,
                        document_text,
                        self._llm
                    )

                elif tool == "quiz":

                    tool_results["quiz"] = generate_quiz(
                        goal,
                        document_text,
                        self._llm
                    )

                elif tool == "report":

                    tool_results["report"] = create_report(
                        goal,
                        document_text,
                        self._llm
                    )

                execution.append(
                    f"{tool} tool completed."
                )

            except Exception as e:

                tool_results[tool] = {
                    "status": "error",
                    "message": str(e)
                }

                execution.append(
                    f"{tool} tool encountered an error."
                )

        # STEP 4: Final synthesis

        execution.append(
            "AI agent is synthesizing the final answer..."
        )

        synthesis_prompt = f"""
You are the final reasoning engine of an autonomous AI agent.

User goal:
{goal}

Agent plan:
{json.dumps(plan)}

Tools executed:
{json.dumps(tools)}

Tool results:
{json.dumps(tool_results, default=str)}

Create a clear final answer for the user.

Use headings and bullet points where useful.

Do not mention internal errors unless they affect the result.

Do not say that you are only a chatbot.

Present the result as the completed work of the AI agent.
"""

        try:

            final_result = self._llm(
                "You are the final response engine of NEXUS AI Agent.",
                synthesis_prompt
            )

        except Exception:

            final_result = (
                "The agent completed its processing, but the "
                "final response could not be generated."
            )

        execution.append(
            "Final result generated."
        )

        return {
            "plan": plan,
            "tools": tools,
            "execution": execution,
            "final_result": final_result
        }
