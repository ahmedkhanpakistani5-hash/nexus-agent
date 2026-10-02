import streamlit as st
from agent import NexusAgent

# =========================================================
# PAGE CONFIG
# =========================================================

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

.stApp {
    background:
        radial-gradient(
            circle at 10% 5%,
            rgba(139, 92, 246, 0.22),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(239, 68, 68, 0.15),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(34, 197, 94, 0.12),
            transparent 25%
        ),
        #050711;

    color: #f8fafc;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

.block-container {
    max-width: 1450px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0b0615,
            #10091f,
            #060a13
        );

    border-right: 1px solid rgba(139, 92, 246, 0.30);
}


/* =========================================================
   SIDEBAR AVATAR
   ========================================================= */

.avatar {
    text-align: center;

    font-size: 70px;

    padding: 15px;

    filter:
        drop-shadow(
            0 0 20px rgba(168, 85, 247, 0.8)
        );
}


/* =========================================================
   SIDEBAR NEXUS TITLE
   ========================================================= */

.sidebar-nexus-title {
    text-align: center;

    font-size: 32px;

    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #c084fc,
            #f472b6,
            #ef4444,
            #4ade80,
            #22d3ee
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.sidebar-nexus-subtitle {
    text-align: center;

    color: #94a3b8;

    font-size: 11px;

    letter-spacing: 3px;
}


/* =========================================================
   GLOWING MAIN NEXUS HEADER
   ========================================================= */

.nexus-header {
    text-align: center;

    padding: 25px 20px 30px 20px;

    margin-bottom: 15px;

    position: relative;
}


/* Purple glow behind header */

.nexus-header::before {

    content: "";

    position: absolute;

    top: -80px;

    left: 50%;

    transform: translateX(-50%);

    width: 650px;

    height: 210px;

    background:
        radial-gradient(
            ellipse,
            rgba(168, 85, 247, 0.38),
            rgba(124, 58, 237, 0.18),
            transparent 70%
        );

    filter: blur(28px);

    pointer-events: none;

    z-index: 0;
}


/* Main glowing title */

.nexus-glow-title {

    position: relative;

    z-index: 1;

    font-size: 50px;

    font-weight: 800;

    letter-spacing: -1px;

    background:
        linear-gradient(
            90deg,
            #f3e8ff,
            #d8b4fe,
            #a855f7,
            #c084fc,
            #f5d0fe
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 10px rgba(168, 85, 247, 0.8),
        0 0 25px rgba(168, 85, 247, 0.55),
        0 0 50px rgba(124, 58, 237, 0.35);

    animation:
        nexusGlow 3s ease-in-out infinite;
}


/* Subtitle */

.nexus-glow-subtitle {

    position: relative;

    z-index: 1;

    margin-top: 8px;

    font-size: 14px;

    font-weight: 600;

    letter-spacing: 5px;

    text-transform: uppercase;

    color: #c4b5fd;

    text-shadow:
        0 0 10px rgba(167, 139, 250, 0.65),
        0 0 25px rgba(139, 92, 246, 0.35);
}


/* Description */

.nexus-description {

    position: relative;

    z-index: 1;

    max-width: 720px;

    margin: 14px auto 0 auto;

    color: #94a3b8;

    font-size: 14px;

    line-height: 1.7;
}


/* Glow animation */

@keyframes nexusGlow {

    0% {

        text-shadow:
            0 0 10px rgba(168, 85, 247, 0.65),
            0 0 25px rgba(168, 85, 247, 0.40),
            0 0 45px rgba(124, 58, 237, 0.20);
    }

    50% {

        text-shadow:
            0 0 15px rgba(192, 132, 252, 0.95),
            0 0 35px rgba(168, 85, 247, 0.70),
            0 0 65px rgba(124, 58, 237, 0.45);
    }

    100% {

        text-shadow:
            0 0 10px rgba(168, 85, 247, 0.65),
            0 0 25px rgba(168, 85, 247, 0.40),
            0 0 45px rgba(124, 58, 237, 0.20);
    }
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {

    font-size: 21px;

    font-weight: 700;

    margin-top: 25px;

    margin-bottom: 12px;

    color: #f8fafc;
}


/* =========================================================
   TEXT AREA
   ========================================================= */

textarea {

    background-color:
        #090d19 !important;

    color:
        white !important;

    border:
        1px solid rgba(139, 92, 246, 0.45) !important;

    border-radius:
        16px !important;

    box-shadow:
        0 0 20px rgba(139, 92, 246, 0.05) !important;
}


/* =========================================================
   FILE UPLOADER
   ========================================================= */

[data-testid="stFileUploader"] {

    background:
        rgba(15, 23, 42, 0.65);

    border:
        1px dashed rgba(34, 211, 238, 0.45);

    border-radius:
        16px;

    padding:
        10px;
}


/* =========================================================
   RUN BUTTON
   ========================================================= */

.stButton > button {

    border:
        none;

    border-radius:
        15px;

    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #db2777,
            #ef4444
        );

    color:
        white;

    font-weight:
        800;

    padding:
        14px;

    transition:
        0.25s;
}

.stButton > button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 10px 35px rgba(168, 85, 247, 0.35);
}


/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

.stDownloadButton > button {

    border-radius:
        14px;

    background:
        rgba(34, 197, 94, 0.12);

    color:
        #86efac;

    border:
        1px solid rgba(34, 197, 94, 0.35);

    font-weight:
        700;
}


/* =========================================================
   EXECUTION TRACE
   ========================================================= */

.execution-item {

    background:
        rgba(15, 23, 42, 0.75);

    border-left:
        3px solid #a855f7;

    border-radius:
        10px;

    padding:
        12px 16px;

    margin-bottom:
        8px;

    color:
        #cbd5e1;
}


/* =========================================================
   FOOTER
   ========================================================= */

.nexus-footer {

    text-align:
        center;

    color:
        #64748b;

    font-size:
        12px;

    margin-top:
        50px;

    padding-top:
        20px;

    border-top:
        1px solid rgba(255,255,255,0.08);
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

if "example_goal" not in st.session_state:
    st.session_state.example_goal = ""


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="avatar">🤖</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-nexus-title">NEXUS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-nexus-subtitle">'
        'AUTONOMOUS AI AGENT'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### ⚡ Capabilities")

    st.markdown("""
    🧠 Intelligent Planning

    📄 Document Analysis

    📚 Study Planning

    📝 Quiz Generation

    📊 Report Generation

    🔧 Autonomous Tool Execution
    """)

    st.divider()

    st.markdown("### 💡 Example Goals")

    examples = [
        "Create a study plan from this document",
        "Analyze this PDF and create a quiz",
        "Generate a report from this document",
        "Help me prepare for my exam"
    ]

    for example in examples:

        if st.button(
            example,
            key=example,
            use_container_width=True
        ):

            st.session_state.example_goal = example

            st.rerun()


# =========================================================
# GLOWING MAIN HEADER
# =========================================================

st.markdown("""
<div class="nexus-header">

    <div class="nexus-glow-title">
        🤖 NEXUS AI Agent
    </div>

    <div class="nexus-glow-subtitle">
        AUTONOMOUS AI PRODUCTIVITY AGENT
    </div>

    <div class="nexus-description">
        Give NEXUS a goal. It decides what to do,
        executes the required tools, and generates the final result.
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# STATUS
# =========================================================

status1, status2, status3 = st.columns(3)

with status1:
    st.success("🟢 AI AGENT — ONLINE")

with status2:
    st.info("🧠 AI PLANNER — READY")

with status3:
    st.error("⚡ TOOLS — READY")


# =========================================================
# GOAL INPUT
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🎯 What should the AI Agent accomplish?'
    '</div>',
    unsafe_allow_html=True
)

goal = st.text_area(
    "Goal",
    value=st.session_state.example_goal,
    height=120,
    placeholder="Example: Analyze this document and create a study plan.",
    label_visibility="collapsed"
)


# =========================================================
# FILE UPLOAD
# =========================================================

st.markdown(
    '<div class="section-title">'
    '📎 Upload Knowledge'
    '</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"],
    label_visibility="collapsed"
)

if uploaded_file:

    st.success(
        f"📄 {uploaded_file.name} uploaded successfully."
    )


# =========================================================
# RUN AGENT
# =========================================================

st.markdown("")

run_left, run_middle, run_right = st.columns(
    [1, 2, 1]
)

with run_middle:

    run_agent = st.button(
        "🚀 RUN AI AGENT",
        use_container_width=True
    )


# =========================================================
# AGENT EXECUTION
# =========================================================

if run_agent:

    if not goal.strip():

        st.warning(
            "Please enter a goal for the AI Agent."
        )

        st.stop()

    try:

        with st.status(
            "🤖 NEXUS AI Agent is working...",
            expanded=True
        ) as status:

            st.write(
                "🧠 AI Agent is understanding your goal..."
            )

            agent = NexusAgent()

            st.write(
                "🔮 AI Agent is deciding which tools are required..."
            )

            result = agent.run(
                goal=goal,
                uploaded_file=uploaded_file
            )

            st.write(
                "⚙️ AI Agent is executing the selected tools..."
            )

            st.write(
                "✨ AI Agent is generating the final result..."
            )

            status.update(
                label="🟢 AI Agent completed the task!",
                state="complete",
                expanded=False
            )

        st.session_state.latest_result = (
            result["final_result"]
        )

        st.session_state.execution = (
            result["execution"]
        )

        st.session_state.plan = (
            result["plan"]
        )

        st.session_state.tools = (
            result["tools"]
        )

    except ValueError as e:

        st.error(
            f"Configuration error: {e}"
        )

    except Exception:

        st.error(
            "The AI Agent could not complete the task. "
            "Please check your API configuration and try again."
        )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.latest_result:

    st.divider()

    # =====================================================
    # EXECUTION TRACE
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '⚡ AI Agent Execution'
        '</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.execution:

        st.markdown(
            f"""
            <div class="execution-item">
                🤖 {item}
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # FINAL RESULT
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '✨ AI Agent Final Result'
        '</div>',
        unsafe_allow_html=True
    )

    st.success(
        "🟢 AI Agent completed the task successfully."
    )

    st.markdown(
        st.session_state.latest_result
    )


    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.download_button(
        "⬇️ DOWNLOAD AI AGENT RESULT",
        data=st.session_state.latest_result,
        file_name="nexus_ai_agent_result.txt",
        mime="text/plain",
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="nexus-footer">

    🤖 NEXUS AI Agent

    <br><br>

    <span style="color:#a78bfa;">
        Goal
    </span>

    →

    <span style="color:#c084fc;">
        Think
    </span>

    →

    <span style="color:#f87171;">
        Decide
    </span>

    →

    <span style="color:#4ade80;">
        Execute
    </span>

    →

    <span style="color:#22d3ee;">
        Synthesize
    </span>

</div>
""", unsafe_allow_html=True)
