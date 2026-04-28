import streamlit as st
import pandas as pd
import time

from instruction_parser import parse_trace
from pipeline_simulator import simulate_pipeline
from hazard_detector import analyze_hazards
from metrics import compute_ideal_cycles, compute_efficiency
from bottleneck_detector import detect_bottleneck
from cycle_model import get_latency

# --- PAGE CONFIG ---
st.set_page_config(page_title="CPU Analyzer", layout="wide")

# --- SESSION STATE ---
if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = False
    st.session_state.trace_data = None

# --- CUSTOM CSS ---
st.markdown("""
<style>
body {
    background-color: #0a0a0a;
    color: #00f2ff;
    font-family: 'Courier New', monospace;
}

header, footer {visibility: hidden;}

.upload-box {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0,255,255,0.3);
    border-radius: 15px;
    padding: 30px;
    text-align: center;
}

.code-text {
    color: #00ff41;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    line-height: 1.6;
    white-space: pre-wrap;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 🚀 LANDING PAGE
# =========================================================
if not st.session_state.file_uploaded:

    col1, col2 = st.columns([1.2, 1])

    # --- LEFT SIDE ---
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1518770660439-4636190af475",
            width=700
        )

        # Short typing description (3–4 lines)
        description = """Initializing CPU Bottleneck Analyzer...

Analyzes instruction traces to detect pipeline stalls,
data dependencies, and execution bottlenecks.

Provides cycle-level insights into CPU performance behavior.
"""

        placeholder = st.empty()
        typed_text = ""

        for char in description:
            typed_text += char
            placeholder.markdown(
                f"<div class='code-text'>{typed_text}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.003)

    # --- RIGHT SIDE ---
    with col2:
        st.markdown("<div class='upload-box'>", unsafe_allow_html=True)

        st.markdown("<h1>CPU Bottleneck Analyzer</h1>", unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload Instruction Trace (.txt)", type=["txt"])

        if uploaded_file is not None:
            content = uploaded_file.read().decode("utf-8")
            st.session_state.trace_data = content.strip().split("\n")
            st.session_state.file_uploaded = True
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# 🧠 ANALYSIS DASHBOARD
# =========================================================
else:
    trace = st.session_state.trace_data
    instructions = parse_trace(trace)

    sim = simulate_pipeline(instructions)
    hazards = analyze_hazards(sim)

    ideal = compute_ideal_cycles(instructions, get_latency)
    actual = sim["total_cycles"]
    eff = compute_efficiency(ideal, actual)
    bottleneck = detect_bottleneck(hazards)

    # Header
    st.markdown("<h1 style='color:#00f2ff'>CPU Bottleneck Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#00ff41'>System Status: ONLINE</h4>", unsafe_allow_html=True)

    # Reset
    if st.button("Analyze New File"):
        st.session_state.file_uploaded = False
        st.session_state.trace_data = None
        st.rerun()

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ideal Cycles", ideal)
    col2.metric("Actual Cycles", actual)
    col3.metric("Efficiency (%)", f"{eff:.2f}")
    col4.metric("Bottleneck", bottleneck)

    # Hazards
    st.markdown("### Hazard Analysis")
    h1, h2, h3, h4, h5 = st.columns(5)

    h1.metric("RAW Stall Cycles", hazards["RAW Stall Cycles"])
    h2.metric("Memory Stalls", hazards["Memory Stall Cycles"])
    h3.metric("Branch Penalty", hazards["Branch Penalty Cycles"])
    h4.metric("WAR Hazards", hazards["WAR Hazards"])
    h5.metric("WAW Hazards", hazards["WAW Hazards"])

    # Tabs
    tab1, tab2 = st.tabs(["Telemetry", "Logs"])

    with tab1:
        df = pd.DataFrame({
            "Instruction": range(len(sim["timeline"])),
            "Stall Cycles": [t["stall"] for t in sim["timeline"]]
        })
        st.line_chart(df.set_index("Instruction"))

    with tab2:
        for i, t in enumerate(sim["timeline"]):
            inst = t["inst"]
            st.write(
                f"[{i}] {inst['opcode']} | ISSUE:{t['issue']} | COMPLETE:{t['complete']} | STALL:{t['stall']}"
            )