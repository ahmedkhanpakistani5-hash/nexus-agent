import streamlit as st
from agent import NexusAgent

st.set_page_config(
    page_title="NEXUS AI Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(124, 58, 237, 0.18), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(6, 182, 212, 0.13), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(79, 70, 229, 0.12), transparent 35%),
        #070b18;
    color: #f8fafc;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            rgba(13, 18, 38, 0.98),
            rgba(7, 11, 24, 0.98)
        );
    border-right: 1px solid rgba(139, 92, 246, 0.18);
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}

/* Main container */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Hero */

.hero {
    padding: 35px 35px 30px 35px;
    border-radius: 28px;
    background:
        linear-gradient(
            135deg,
            rgba(124, 58, 237, 0.18),
            rgba(6, 182, 212, 0.08)
        );
    border: 1px solid rgba(139, 92, 246, 0.25);
    box-shadow:
        0 0 50px rgba(124, 58, 237, 0.10),
        inset 0 1px 0 rgba(255,255,255,0.04);
    margin-bottom: 25px;
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 30px;
    background: rgba(6, 182, 212, 0.10);
    border: 1px solid rgba(6, 182, 212, 0.30);
    color: #67e8f9;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 15px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin: 0;
    letter-spacing: -2px;
    background: linear-gradient(
        90deg,
        #ffffff,
        #c4b5fd,
        #67e8f9
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #94a3b8;
    font-size: 16px;
    margin-top: 10px;
}

/* Section titles */

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 12px;
    color: #f8fafc;
}

/* Glass cards */

.glass-card {
    background: rgba(15, 23, 42, 0.68);
    border: 1px solid rgba(148, 163, 184, 0.12);
    border-radius: 20px;
    padding: 22px;
    box-shadow:
        0 15px 40px rgba(0,0,0,0.22),
        inset 0 1px 0 rgba(255,255,255,0.025);
}

/* Status cards */

.status-card {
    background: linear-gradient(
        135deg,
        rgba(16, 185, 129, 0.10),
        rgba(15, 23, 42, 0.75)
    );
    border: 1px solid rgba(16, 185, 129, 0.22);
    border-radius: 18px;
    padding: 17px;
    text-align: center;
}

.status-dot {
    display: inline-block;
    width: 9px;
    height: 9px;
    background: #34d399;
    border-radius: 50%;
    box-shadow: 0 0 12px #34d399;
    margin-right: 7px;
}

/* Text areas */

textarea {
    background: rgba(8, 15, 32, 0.90) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(139, 92, 246, 0.25) !important;
    border-radius: 16px !important;
}

/* File uploader */

[data-testid="stFileUploader"] {
    background: rgba(15, 23, 42, 0.55);
    border-radius: 18px;
    border: 1px dashed rgba(103, 232, 249, 0.30);
    padding: 8px;
}

/* Buttons */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(139, 92, 246, 0.40);
    background: linear-gradient(
        135deg,
        #7c3aed,
        #4f46e5
    );
    color: white;
    font-weight: 700;
    font-size: 15px;
    padding: 13px 20px;
    transition: all 0.25s ease;
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.22);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 12px 35px rgba(124, 58, 237, 0.38);
    border-color: #a78bfa;
}

/* Download button */

.stDownloadButton > button {
    width: 100%;
    border-radius: 14px;
    background: rgba(15, 23, 42, 0.8);
    color: #67e8f9;
    border: 1px solid rgba(103, 232, 249, 0.30);
    font-weight: 600;
}

/* Expanders */

.streamlit-expanderHeader {
    background: rgba(15, 23, 42, 0.65) !important;
    border-radius: 14px !important;
}

/* Tool pills */

.tool-pill {
    display: inline-block;
    padding: 8px 13px;
    margin: 4px;
    border-radius: 20px;
    background: rgba(124, 58, 237, 0.13);
    border: 1px solid rgba(139, 92, 246, 0.28);
    color: #c4b5fd;
    font-size: 13px;
    font-weight: 600;
}

/* Timeline */

.timeline-item {
    padding: 13px 16px;
    margin: 7px 0;
    border-left: 3px solid #8b5cf6;
    background: rgba(15, 23, 42, 0.55);
    border-radius: 0 12px 12px 0;
    color: #cbd5e1;
}

/* Footer */

.nexus-footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid rgba(148,163,184,0.08);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "latest_result" not in st.session_state:
    st.session_state.latest_result = None

if "execution" not in st.session_state:
    st.session_state.execution = []

if "plan" not in st.session_state:
    st.session_state.plan = []

if "tools" not in st.session_state:
    st.session_state.tools = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div style="
        text-align:center;
        padding:15px 5px 25px 5px;
    ">
        <div style="
            font-size:45px;
            margin-bottom:8px;
        ">◈</div>

        <div style="
            font-size:23px;
            font-weight:800;
            color:#f8fafc;
        ">NEXUS</div>

        <div style="
            color:#8b5cf6;
            font-size:12px;
            font-weight:600;
            letter-spacing:2px;
        ">AUTONOMOUS AI</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### ⚡ Agent Capabilities")

    st.markdown("""
    **🧠 Intelligent Planning**  
    Converts goals into actionable plans.

    **📄 Document Intelligence**  
    Reads PDF, DOCX and TXT files.

    **📚 Study Planning**  
    Creates personalized study plans.

    **📝 Quiz Generation**  
    Generates 10-question MCQ quizzes.

    **📊 Report Generation**  
    Produces structured reports.

    **🔧 Tool Execution**  
    Selects and executes the required tools.
    """)

    st.markdown("---")

    st.markdown("### 💡 Example Goals")

    examples = [
        "Create a study plan from this document",
        "Analyze this PDF and create a quiz",
        "Generate a detailed report from this document",
        "Help me prepare for my exam"
    ]

    for example in examples:
        if st.button(example, key=example):
            st.session_state.example_goal = example

    st.markdown("---")

    st.markdown("""
    <div style="
        text-align:center;
        color:#64748b;
        font-size:11px;
    ">
        NEXUS AI Agent<br>
        Hackathon Edition
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        ● AUTONOMOUS AI AGENT
    </div>

    <h1>NEXUS AI Agent</h1>

    <p>
        Transform your goal into an intelligent plan,
        execute the right tools, and receive a complete result.
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# STATUS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="status-card">
        <span class="status-dot"></span>
        <b>Agent Online</b>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="status-card">
        🧠 <b>AI Planning Ready</b>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="status-card">
        ⚙️ <b>Tools Ready</b>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# GOAL INPUT
# =========================================================

st.markdown(
    '<div class="section-title">🎯 What do you want NEXUS to accomplish?</div>',
    unsafe_allow_html=True
)

default_goal = st.session_state.get("example_goal", "")

goal = st.text_area(
    "Goal",
    value=default_goal,
    height=120,
    placeholder=(
        "Example: Analyze my uploaded lecture notes, "
        "create a 7-day study plan and generate a quiz..."
    ),
    label_visibility="collapsed"
)


# =========================================================
# FILE UPLOAD
# =========================================================

st.markdown(
    '<div class="section-title">📎 Give your agent a document (optional)</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"],
    label_visibility="collapsed"
)

if uploaded_file:
    st.success(
        f"📄 {uploaded_file.name} is ready for NEXUS."
    )


# =========================================================
# RUN AGENT
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

run_col1, run_col2, run_col3 = st.columns([1, 2, 1])

with run_col2:

    run_agent = st.button(
        "🚀  RUN NEXUS AGENT",
        use_container_width=True
    )


if run_agent:

    if not goal.strip():
        st.warning(
            "Please enter a goal before running the agent."
        )
        st.stop()

    try:

        with st.status(
            "🤖 NEXUS is working...",
            expanded=True
        ) as status:

            st.write("🧠 Understanding your goal...")

            agent = NexusAgent()

            st.write("📋 Creating execution plan...")

            result = agent.run(
                goal=goal,
                uploaded_file=uploaded_file
            )

            st.write("🔧 Executing selected tools...")

            st.write("✨ Synthesizing final result...")

            status.update(
                label="✅ NEXUS completed successfully!",
                state="complete",
                expanded=False
            )

        st.session_state.latest_result = result["final_result"]
        st.session_state.execution = result["execution"]
        st.session_state.plan = result["plan"]
        st.session_state.tools = result["tools"]

    except ValueError as e:

        st.error(f"Configuration error: {e}")

    except Exception:

        st.error(
            "NEXUS could not complete the request. "
            "Please check your goal, uploaded file, and API configuration."
        )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.latest_result:

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">⚡ Agent Execution</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.execution:

        st.markdown(
            f"""
            <div class="timeline-item">
                ✓ {item}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Plan + tools

    left, right = st.columns(2)

    with left:

        st.markdown(
            '<div class="section-title">🧠 Agent Plan</div>',
            unsafe_allow_html=True
        )

        for i, step in enumerate(
            st.session_state.plan,
            1
        ):

            st.markdown(
                f"""
                <div class="glass-card" style="margin-bottom:8px;">
                    <b style="color:#a78bfa;">STEP {i}</b><br>
                    <span style="color:#cbd5e1;">
                        {step}
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    with right:

        st.markdown(
            '<div class="section-title">🔧 Tools Selected</div>',
            unsafe_allow_html=True
        )

        tool_html = ""

        for tool in st.session_state.tools:

            tool_html += (
                f'<span class="tool-pill">⚙ {tool}</span>'
            )

        st.markdown(
            f"""
            <div class="glass-card">
                {tool_html}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Final result

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">✨ Final Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="glass-card">
            {st.session_state.latest_result}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.download_button(
        "⬇️ Download Result",
        data=st.session_state.latest_result,
        file_name="nexus_result.txt",
        mime="text/plain"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="nexus-footer">
    NEXUS AI Agent • Plan → Select → Execute → Synthesize
</div>
""", unsafe_allow_html=True)
