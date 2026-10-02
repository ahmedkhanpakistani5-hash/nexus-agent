import streamlit as st
from agent import NexusAgent

st.set_page_config(
    page_title="NEXUS AI Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# NEXUS COLORFUL UI
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, rgba(168, 85, 247, 0.22), transparent 25%),
        radial-gradient(circle at 95% 10%, rgba(239, 68, 68, 0.16), transparent 25%),
        radial-gradient(circle at 85% 85%, rgba(34, 197, 94, 0.13), transparent 25%),
        radial-gradient(circle at 15% 90%, rgba(6, 182, 212, 0.12), transparent 25%),
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
            #0c0718 0%,
            #10091f 50%,
            #070b15 100%
        );

    border-right: 1px solid rgba(168, 85, 247, 0.25);
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb;
}


/* =========================================================
   AI AVATAR
   ========================================================= */

.ai-avatar {
    width: 105px;
    height: 105px;
    margin: 5px auto 15px auto;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #c084fc,
            #7c3aed 45%,
            #4c1d95 100%
        );

    border: 3px solid rgba(255,255,255,0.15);

    box-shadow:
        0 0 20px rgba(168,85,247,0.7),
        0 0 60px rgba(168,85,247,0.35);

    font-size: 50px;

    animation: pulse 3s infinite;
}

@keyframes pulse {

    0% {
        box-shadow:
            0 0 20px rgba(168,85,247,0.7),
            0 0 50px rgba(168,85,247,0.25);
    }

    50% {
        box-shadow:
            0 0 30px rgba(168,85,247,0.9),
            0 0 80px rgba(168,85,247,0.4);
    }

    100% {
        box-shadow:
            0 0 20px rgba(168,85,247,0.7),
            0 0 50px rgba(168,85,247,0.25);
    }
}


/* =========================================================
   NEXUS TITLE
   ========================================================= */

.nexus-title {
    text-align: center;

    font-size: 31px;
    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #c084fc,
            #f472b6,
            #fb7185,
            #4ade80,
            #22d3ee
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nexus-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    letter-spacing: 3px;
}


/* =========================================================
   STATUS CARDS
   ========================================================= */

.status-card {
    border-radius: 18px;
    padding: 18px;

    text-align: center;

    background: rgba(15,23,42,0.70);

    backdrop-filter: blur(15px);

    transition: 0.25s;
}

.status-card:hover {
    transform: translateY(-3px);
}


/* GREEN */

.status-green {
    border: 1px solid rgba(34,197,94,0.35);

    box-shadow:
        0 0 25px rgba(34,197,94,0.08);
}


/* PURPLE */

.status-purple {
    border: 1px solid rgba(168,85,247,0.40);

    box-shadow:
        0 0 25px rgba(168,85,247,0.10);
}


/* RED */

.status-red {
    border: 1px solid rgba(239,68,68,0.35);

    box-shadow:
        0 0 25px rgba(239,68,68,0.08);
}


/* =========================================================
   SECTION TITLE
   ========================================================= */

.section-title {
    font-size: 21px;
    font-weight: 700;

    margin-top: 25px;
    margin-bottom: 12px;
}


/* =========================================================
   INPUT
   ========================================================= */

textarea {
    background:
        rgba(8, 10, 25, 0.95) !important;

    color: white !important;

    border:
        1px solid rgba(168,85,247,0.35) !important;

    border-radius: 18px !important;

    box-shadow:
        0 0 25px rgba(168,85,247,0.05) !important;
}


/* =========================================================
   FILE UPLOADER
   ========================================================= */

[data-testid="stFileUploader"] {

    background:
        linear-gradient(
            135deg,
            rgba(168,85,247,0.08),
            rgba(6,182,212,0.06)
        );

    border:
        1px dashed rgba(34,211,238,0.45);

    border-radius: 18px;

    padding: 10px;
}


/* =========================================================
   MAIN RUN BUTTON
   ========================================================= */

.stButton > button {

    width: 100%;

    border: none;

    border-radius: 16px;

    padding: 14px;

    font-size: 15px;

    font-weight: 800;

    color: white;

    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #db2777,
            #ef4444
        );

    box-shadow:
        0 8px 30px rgba(168,85,247,0.25);

    transition: all 0.25s ease;
}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 12px 40px rgba(236,72,153,0.35);

    border: none;
}


/* =========================================================
   DOWNLOAD BUTTON
   ========================================================= */

.stDownloadButton > button {

    width: 100%;

    border-radius: 14px;

    background:
        linear-gradient(
            90deg,
            rgba(34,197,94,0.15),
            rgba(6,182,212,0.12)
        );

    color: #86efac;

    border:
        1px solid rgba(34,197,94,0.35);

    font-weight: 700;
}


/* =========================================================
   GLASS CARD
   ========================================================= */

.glass-card {

    background:
        linear-gradient(
            135deg,
            rgba(20,20,40,0.85),
            rgba(10,15,30,0.72)
        );

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 22px;

    box-shadow:
        0 15px 45px rgba(0,0,0,0.25);

    backdrop-filter: blur(15px);
}


/* =========================================================
   EXECUTION TIMELINE
   ========================================================= */

.timeline-item {

    padding: 14px 17px;

    margin: 8px 0;

    border-radius: 13px;

    background:
        linear-gradient(
            90deg,
            rgba(168,85,247,0.10),
            rgba(15,23,42,0.55)
        );

    border-left:
        3px solid #a855f7;

    color: #cbd5e1;
}


/* =========================================================
   FINAL RESULT
   ========================================================= */

.result-card {

    background:
        linear-gradient(
            135deg,
            rgba(34,197,94,0.08),
            rgba(168,85,247,0.10),
            rgba(15,23,42,0.80)
        );

    border:
        1px solid rgba(34,197,94,0.22);

    border-radius: 22px;

    padding: 28px;

    box-shadow:
        0 0 40px rgba(34,197,94,0.06);
}


/* =========================================================
   FOOTER
   ========================================================= */

.nexus-footer {

    text-align: center;

    color: #64748b;

    font-size: 12px;

    margin-top: 50px;

    padding-top: 20px;

    border-top:
        1px solid rgba(255,255,255,0.06);
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
    <div class="ai-avatar">
        🤖
    </div>

    <div class="nexus-title">
        NEXUS
    </div>

    <div class="nexus-subtitle">
        AUTONOMOUS AI
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### ⚡ Agent Capabilities")

    st.markdown("""
    🧠 **Intelligent Planning**

    📄 **Document Intelligence**

    📚 **Study Planning**

    📝 **Quiz Generation**

    📊 **Report Generation**

    🔧 **Autonomous Tool Execution**
    """)

    st.markdown("---")

    st.markdown("### 💡 Quick Goals")

    examples = [
        "Create a study plan from this document",
        "Analyze this PDF and create a quiz",
        "Generate a detailed report from this document",
        "Help me prepare for my exam"
    ]

    for example in examples:

        if st.button(
            example,
            key=example
        ):

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
# STATUS CARDS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="status-card status-green">

        🟢

        <br>

        <b>AGENT ONLINE</b>

        <br>

        <span style="color:#86efac;font-size:12px;">
        System Ready
        </span>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="status-card status-purple">

        🧠

        <br>

        <b>AI PLANNER</b>

        <br>

        <span style="color:#c084fc;font-size:12px;">
        Decision Engine Ready
        </span>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="status-card status-red">

        ⚡

        <br>

        <b>TOOLS READY</b>

        <br>

        <span style="color:#fca5a5;font-size:12px;">
        Execution Available
        </span>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# GOAL INPUT
# =========================================================

st.markdown(
    '<div class="section-title">🎯 What do you want NEXUS to accomplish?</div>',
    unsafe_allow_html=True
)

default_goal = st.session_state.get(
    "example_goal",
    ""
)

goal = st.text_area(
    "Goal",
    value=default_goal,
    height=120,
    placeholder=(
        "Tell NEXUS what you want to accomplish..."
    ),
    label_visibility="collapsed"
)


# =========================================================
# FILE UPLOAD
# =========================================================

st.markdown(
    '<div class="section-title">📎 Upload Knowledge</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"],
    label_visibility="collapsed"
)

if uploaded_file:

    st.success(
        f"📄 {uploaded_file.name} loaded successfully."
    )


# =========================================================
# RUN AGENT
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

run_col1, run_col2, run_col3 = st.columns(
    [1, 2, 1]
)

with run_col2:

    run_agent = st.button(
        "🚀 RUN NEXUS AGENT",
        use_container_width=True
    )


if run_agent:

    if not goal.strip():

        st.warning(
            "Please enter a goal first."
        )

        st.stop()

    try:

        with st.status(
            "🔴 NEXUS is thinking...",
            expanded=True
        ) as status:

            st.write(
                "🧠 Understanding your goal..."
            )

            agent = NexusAgent()

            st.write(
                "🟣 Creating execution plan..."
            )

            result = agent.run(
                goal=goal,
                uploaded_file=uploaded_file
            )

            st.write(
                "🔵 Executing selected tools..."
            )

            st.write(
                "🟢 Synthesizing final result..."
            )

            status.update(
                label="🟢 NEXUS completed successfully!",
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
            "NEXUS could not complete the request. "
            "Please check your goal, document and API configuration."
        )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.latest_result:

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # EXECUTION TRACE
    # =====================================================

    st.markdown(
        '<div class="section-title">⚡ Agent Execution Trace</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.execution:

        st.markdown(
            f"""
            <div class="timeline-item">
                🟣 {item}
            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # FINAL RESULT
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">✨ NEXUS Final Result</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="result-card">

            <div style="
                color:#86efac;
                font-size:13px;
                font-weight:700;
                margin-bottom:15px;
            ">
                🟢 TASK COMPLETED
            </div>

            <div style="
                color:#e2e8f0;
                line-height:1.8;
            ">
                {st.session_state.latest_result}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.download_button(
        "⬇️ DOWNLOAD RESULT",
        data=st.session_state.latest_result,
        file_name="nexus_result.txt",
        mime="text/plain"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="nexus-footer">

    🤖 NEXUS AI Agent

    <br>

    <span style="color:#8b5cf6;">
        Plan
    </span>

    →

    <span style="color:#ef4444;">
        Decide
    </span>

    →

    <span style="color:#22c55e;">
        Execute
    </span>

    →

    <span style="color:#22d3ee;">
        Synthesize
    </span>

</div>
""", unsafe_allow_html=True)
