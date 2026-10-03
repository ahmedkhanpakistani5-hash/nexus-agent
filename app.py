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
            circle at 10% 10%,
            rgba(139, 92, 246, 0.20),
            transparent 25%
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
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* TOP HEADER BAR */

header[data-testid="stHeader"] {
    background: rgba(5, 7, 17, 0.65);
    backdrop-filter: blur(8px);
    border-bottom: 1px solid rgba(56, 189, 248, 0.40);
    box-shadow: 0 2px 20px rgba(56, 189, 248, 0.25);
}

header[data-testid="stHeader"] * {
    color: #7DD3FC !important;
}

header[data-testid="stHeader"] svg {
    fill: #7DD3FC !important;
}
/* NEXUS MAIN TITLE GLOW */

.stApp h1 {
    color: #E0F7FF !important;
    font-weight: 900 !important;
    font-size: 3.4rem !important;
    text-shadow:
        0 0 6px #FFFFFF,
        0 0 12px #7DD3FC,
        0 0 24px #38BDF8,
        0 0 48px #0EA5E9,
        0 0 90px #0284C7;
    animation: titlePulse 3s ease-in-out infinite;
}

/* "Autonomous AI Productivity Agent" line */
.stApp h1 + div p strong,
.stApp [data-testid="stMarkdownContainer"] p strong {
    color: #7DD3FC !important;
    text-shadow: 0 0 12px rgba(56, 189, 248, 0.8);
}

/* "Give NEXUS a goal..." line */
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stCaptionContainer"] p {
    color: #BAE6FD !important;
    opacity: 1 !important;
}

@keyframes titlePulse {
    0%, 100% {
        text-shadow: 0 0 6px #FFFFFF, 0 0 18px #38BDF8, 0 0 40px #0EA5E9;
    }
    50% {
        text-shadow: 0 0 10px #FFFFFF, 0 0 28px #7DD3FC, 0 0 60px #38BDF8, 0 0 110px #0284C7;
    }
}

.stApp h1,
.stApp h1 span,
.stApp h1 div {
    font-size: 3.4rem !important;
    line-height: 1.2 !important;
}
.block-container {
    max-width: 1450px;
    ...
}

/* SIDEBAR */

section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    background:
        linear-gradient(
            180deg,
            #0b0615,
            #10091f,
            #060a13
        ) !important;
}

section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(139, 92, 246, 0.30);
}

/* sidebar text: bright and readable */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] li,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #E0F2FE !important;
    opacity: 1 !important;
    font-size: 1rem;
}

/* headings: Capabilities, Example Goals */
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h3 * {
    color: #7DD3FC !important;
    font-weight: 800 !important;
}

/* divider lines */
section[data-testid="stSidebar"] hr {
    border-color: rgba(139, 92, 246, 0.35) !important;
}

/* example goal buttons */
section[data-testid="stSidebar"] .stButton > button {
    background: rgba(139, 92, 246, 0.12) !important;
    color: #E0F2FE !important;
    border: 1px solid rgba(139, 92, 246, 0.45) !important;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(139, 92, 246, 0.25) !important;
    border-color: #A78BFA !important;
    transform: translateY(-2px);
}

/* AVATAR */

.avatar {
    width: 90px;
    height: 90px;

    margin: 10px auto 20px auto;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(59, 130, 246, 0.35),
            rgba(99, 102, 241, 0.18),
            rgba(168, 85, 247, 0.08)
        );

    border: 2px solid rgba(147, 197, 253, 0.65);

    font-size: 48px;

    box-shadow:
        0 0 10px rgba(59, 130, 246, 0.9),
        0 0 25px rgba(59, 130, 246, 0.75),
        0 0 50px rgba(99, 102, 241, 0.6),
        0 0 80px rgba(168, 85, 247, 0.45);

    animation: avatarGlow 2.5s ease-in-out infinite;
}

@keyframes avatarGlow {

    0% {
        box-shadow:
            0 0 10px rgba(59, 130, 246, 0.7),
            0 0 25px rgba(59, 130, 246, 0.5),
            0 0 50px rgba(99, 102, 241, 0.35);
    }

    50% {
        box-shadow:
            0 0 15px rgba(96, 165, 250, 1),
            0 0 35px rgba(59, 130, 246, 0.9),
            0 0 65px rgba(99, 102, 241, 0.75),
            0 0 100px rgba(168, 85, 247, 0.5);
    }

    100% {
        box-shadow:
            0 0 10px rgba(59, 130, 246, 0.7),
            0 0 25px rgba(59, 130, 246, 0.5),
            0 0 50px rgba(99, 102, 241, 0.35);
    }
}

/* =========================================================
   NEXUS TITLE — BRIGHT BLUE/PURPLE GLOW
   ========================================================= */

.nexus-title {
    text-align: center;

    font-size: 42px;

    font-weight: 900;

    letter-spacing: 1px;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #dbeafe,
            #93c5fd,
            #a78bfa,
            #e9d5ff,
            #ffffff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 10px rgba(96, 165, 250, 1),
        0 0 25px rgba(59, 130, 246, 0.95),
        0 0 50px rgba(99, 102, 241, 0.8),
        0 0 80px rgba(168, 85, 247, 0.55);

    animation: nexusGlow 3s ease-in-out infinite;
}

@keyframes nexusGlow {

    0% {
        text-shadow:
            0 0 10px rgba(96, 165, 250, 0.8),
            0 0 25px rgba(59, 130, 246, 0.6),
            0 0 50px rgba(99, 102, 241, 0.4);
    }

    50% {
        text-shadow:
            0 0 15px rgba(147, 197, 253, 1),
            0 0 35px rgba(59, 130, 246, 1),
            0 0 70px rgba(99, 102, 241, 0.85),
            0 0 100px rgba(168, 85, 247, 0.6);
    }

    100% {
        text-shadow:
            0 0 10px rgba(96, 165, 250, 0.8),
            0 0 25px rgba(59, 130, 246, 0.6),
            0 0 50px rgba(99, 102, 241, 0.4);
    }
}

.nexus-subtitle {
    text-align: center;

    color: #bfdbfe;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 4px;

    text-shadow:
        0 0 10px rgba(59, 130, 246, 0.8),
        0 0 20px rgba(59, 130, 246, 0.5);
}


/* SECTION */

.section-title {
    font-size: 22px;

    font-weight: 700;

    margin-top: 25px;

    margin-bottom: 12px;

    color: #f8fafc;
}


/* TEXTAREA */

[data-testid="stTextArea"] div,
[data-testid="stTextArea"] [data-baseweb="textarea"],
[data-testid="stTextArea"] [data-baseweb="base-input"] {
    background-color: #070b18 !important;
}

[data-testid="stTextArea"] [data-baseweb="textarea"] {
    border: 1px solid rgba(56, 189, 248, 0.55) !important;
    border-radius: 16px !important;
    box-shadow:
        0 0 12px rgba(56, 189, 248, 0.25),
        inset 0 0 18px rgba(56, 189, 248, 0.06);
    transition: 0.3s;
}

[data-testid="stTextArea"] [data-baseweb="textarea"]:focus-within {
    border: 1px solid #7DD3FC !important;
    box-shadow:
        0 0 18px rgba(56, 189, 248, 0.6),
        0 0 40px rgba(14, 165, 233, 0.35),
        inset 0 0 22px rgba(56, 189, 248, 0.10);
}

[data-testid="stTextArea"] textarea {
    background-color: #070b18 !important;
    color: #E0F7FF !important;
    -webkit-text-fill-color: #E0F7FF !important;
    caret-color: #7DD3FC !important;
    font-size: 1.05rem !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #7DD3FC !important;
    -webkit-text-fill-color: #7DD3FC !important;
    opacity: 0.55 !important;
}
/* FILE UPLOADER */

[data-testid="stFileUploader"] {
    background: rgba(8, 14, 30, 0.7) !important;
    border: 1px dashed rgba(56, 189, 248, 0.6);
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0 0 18px rgba(56, 189, 248, 0.2);
    transition: 0.3s;
}

[data-testid="stFileUploader"]:hover {
    border-color: #7DD3FC;
    box-shadow: 0 0 28px rgba(56, 189, 248, 0.45);
}

/* the light gray area */
[data-testid="stFileUploaderDropzone"],
[data-testid="stFileUploaderDropzone"] > div {
    background-color: #070b18 !important;
    border: 1px solid rgba(56, 189, 248, 0.35) !important;
    border-radius: 14px !important;
}

/* "200MB per file" text */
[data-testid="stFileUploaderDropzone"] small,
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] p,
[data-testid="stFileUploaderDropzoneInstructions"] * {
    color: #BAE6FD !important;
}

/* Upload button */
[data-testid="stFileUploaderDropzone"] button {
    background: linear-gradient(90deg, #0EA5E9, #38BDF8) !important;
    color: #04111f !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 12px !important;
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.5);
    transition: 0.25s;
}

[data-testid="stFileUploaderDropzone"] button:hover {
    box-shadow: 0 0 26px rgba(125, 211, 252, 0.9);
    transform: translateY(-2px);
}

/* uploaded file name row */
[data-testid="stFileUploaderFile"],
[data-testid="stFileUploaderFile"] * {
    color: #E0F7FF !important;
}
/* AI RESULT TEXT */

[data-testid="stMain"] [data-testid="stMarkdownContainer"] p,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] li,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] td {
    color: #E0F2FE !important;
    opacity: 1 !important;
    font-size: 1.02rem;
    line-height: 1.7;
}

/* result headings */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h2,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h3,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h4 {
    color: #7DD3FC !important;
    font-weight: 800 !important;
    text-shadow:
        0 0 8px rgba(56, 189, 248, 0.7),
        0 0 20px rgba(14, 165, 233, 0.4);
}

/* bold text inside results */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] strong {
    color: #BAE6FD !important;
    font-weight: 700;
}

/* tables */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] th {
    color: #7DD3FC !important;
    background: rgba(56, 189, 248, 0.10) !important;
}

[data-testid="stMain"] [data-testid="stMarkdownContainer"] th,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] td {
    border-color: rgba(56, 189, 248, 0.30) !important;
}

/* code blocks and inline code */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] code {
    color: #7DD3FC !important;
    background: rgba(56, 189, 248, 0.10) !important;
}

/* links and horizontal lines */
[data-testid="stMain"] [data-testid="stMarkdownContainer"] a {
    color: #38BDF8 !important;
}

[data-testid="stMain"] hr {
    border-color: rgba(56, 189, 248, 0.30) !important;
}
/* BUTTON */

.stButton > button {

    border: none;

    border-radius: 15px;

    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #db2777,
            #ef4444
        );

    color: white;

    font-weight: 800;

    padding: 14px;

    transition: 0.25s;
}

.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 10px 35px rgba(168, 85, 247, 0.35);
}


/* DOWNLOAD */

.stDownloadButton > button {

    border-radius: 14px;

    background:
        rgba(34, 197, 94, 0.12);

    color: #86efac;

    border:
        1px solid rgba(34, 197, 94, 0.35);
}


/* EXECUTION */

.execution-item {

    background:
        rgba(15, 23, 42, 0.75);

    border-left:
        3px solid #a855f7;

    border-radius: 10px;

    padding: 12px 16px;

    margin-bottom: 8px;

    color: #cbd5e1;
}


/* RESULT */

.result-box {

    background:
        rgba(10, 15, 30, 0.80);

    border:
        1px solid rgba(139, 92, 246, 0.25);

    border-radius: 18px;

    padding: 20px;

    margin-bottom: 10px;
}


/* FOOTER */

.footer {
    text-align: center;

    color: #64748b;

    font-size: 12px;

    margin-top: 50px;

    padding-top: 20px;

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
        '<div class="nexus-title">NEXUS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nexus-subtitle">AUTONOMOUS AI AGENT</div>',
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
# MAIN TITLE
# =========================================================

st.markdown(
    """
    # 🤖 NEXUS AI Agent

    **Autonomous AI Productivity Agent**
    """,
    unsafe_allow_html=True
)

st.caption(
    "Give NEXUS a goal. It decides what to do, executes the required tools, "
    "and generates the final result."
)


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
# GOAL
# =========================================================

st.markdown(
    '<div class="section-title">🎯 What should the AI Agent accomplish?</div>',
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
# FILE
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
        f"📄 {uploaded_file.name} uploaded successfully."
    )


# =========================================================
# RUN
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
        '<div class="section-title">⚡ AI Agent Execution</div>',
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
        '<div class="section-title">✨ AI Agent Final Result</div>',
        unsafe_allow_html=True
    )

    st.success(
        "🟢 AI Agent completed the task successfully."
    )

    # IMPORTANT:
    # The actual AI response is rendered directly by
    # Streamlit. No HTML wrapper around the response.

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

st.markdown(
    """
    <div class="footer">
        🤖 NEXUS AI Agent
        <br><br>
        Goal → Think → Decide → Execute → Synthesize
    </div>
    """,
    unsafe_allow_html=True
)
