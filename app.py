import streamlit as st

from agent import NexusAgent


st.set_page_config(
    page_title="NEXUS AI Agent",
    page_icon="🤖",
    layout="wide"
)


st.markdown("""
<style>
    .stApp {
        background: #0b0f19;
        color: #f5f7ff;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #aeb7cc;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .card {
        background: #111827;
        border: 1px solid #26324a;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
    }

    .status {
        background: #101827;
        border-left: 4px solid #7c3aed;
        padding: 12px 16px;
        border-radius: 8px;
        margin: 6px 0;
    }

    .tool {
        display: inline-block;
        background: #17213a;
        border: 1px solid #35456b;
        border-radius: 20px;
        padding: 7px 13px;
        margin: 4px;
    }

    .success {
        color: #8ef0b2;
    }
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="main-title">🤖 NEXUS AI Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Transform goals into plans, actions and results.</div>',
    unsafe_allow_html=True
)


if "latest_result" not in st.session_state:
    st.session_state.latest_result = ""

if "execution" not in st.session_state:
    st.session_state.execution = []

if "plan" not in st.session_state:
    st.session_state.plan = []

if "tools" not in st.session_state:
    st.session_state.tools = []


with st.sidebar:
    st.header("⚙️ NEXUS")

    st.write(
        "NEXUS is an autonomous productivity agent that "
        "plans tasks, selects tools and combines their results."
    )

    st.divider()

    st.subheader("Example Goals")

    examples = [
        "Analyze this document, identify the most important topics, create a 7-day study plan and generate practice questions.",
        "Read this document and create 10 MCQs with answers.",
        "Analyze this material and create a structured report.",
        "Summarize this material and create an actionable plan."
    ]

    for example in examples:
        st.write("• " + example)


col1, col2 = st.columns([1.5, 1])


with col1:
    st.subheader("🎯 Your Goal")

    goal = st.text_area(
        "Tell NEXUS what you want to accomplish",
        placeholder=(
            "Example: Analyze my lecture notes, identify the important "
            "topics, create a study plan and generate 10 practice questions."
        ),
        height=150
    )


with col2:
    st.subheader("📄 Upload Material")

    uploaded_file = st.file_uploader(
        "Upload PDF, DOCX or TXT",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file:
        st.success(f"Uploaded: {uploaded_file.name}")
    else:
        st.info("Document upload is optional.")


st.divider()


run_agent = st.button(
    "🚀 Run NEXUS Agent",
    type="primary",
    use_container_width=True
)


if run_agent:

    if not goal.strip():
        st.error("Please enter a goal before running the agent.")
        st.stop()

    try:
        agent = NexusAgent()

        st.session_state.execution = []

        progress_placeholder = st.empty()

        progress_placeholder.markdown(
            '<div class="status">🟢 Goal received</div>',
            unsafe_allow_html=True
        )

        document_file = uploaded_file

        result = agent.run(
            goal=goal,
            uploaded_file=document_file
        )

        st.session_state.latest_result = result["final_result"]
        st.session_state.execution = result["execution"]
        st.session_state.plan = result["plan"]
        st.session_state.tools = result["tools"]

        progress_placeholder.empty()

        st.success("✅ NEXUS completed the task successfully.")

    except ValueError as error:
        st.error(str(error))

    except Exception:
        st.error(
            "The AI service could not complete the request. "
            "Please check your Streamlit Secrets and try again."
        )


if st.session_state.execution:

    st.divider()

    st.header("⚡ Agent Execution")

    for step in st.session_state.execution:
        st.markdown(
            f'<div class="status">{step}</div>',
            unsafe_allow_html=True
        )


if st.session_state.plan:

    st.divider()

    st.header("📋 Execution Plan")

    for index, step in enumerate(st.session_state.plan, 1):
        st.write(f"**{index}.** {step}")


if st.session_state.tools:

    st.header("🛠️ Tools Used")

    for tool in st.session_state.tools:
        st.markdown(
            f'<span class="tool">🔧 {tool}</span>',
            unsafe_allow_html=True
        )


if st.session_state.latest_result:

    st.divider()

    st.header("🎯 Final Result")

    st.markdown(st.session_state.latest_result)

    st.download_button(
        label="⬇️ Download Result",
        data=st.session_state.latest_result,
        file_name="nexus_result.md",
        mime="text/markdown",
        use_container_width=True
    )
