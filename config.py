import streamlit as st

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
GROQ_MODEL = st.secrets.get("GROQ_MODEL", "openai/gpt-oss-20b")
