import streamlit as st
import os
import pandas as pd
import subprocess
import plotly.graph_objects as go
import random, time

# ── Page config ────────────────────────────────────────────────
st.set_page_config(page_title="EyeNet – Traffic Control", page_icon="📡", layout="wide")

# Path to CSS (Goes up one level from 'pages' to find 'style.css')
css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session state initialization
if "monitoring" not in st.session_state:
    st.session_state.monitoring = False

if "traffic_gen" not in st.session_state:
    st.session_state.traffic_gen = False

if "last_action" not in st.session_state:
    st.session_state.last_action = "Traffic Control System initialized."

if "sender_process" not in st.session_state:
    st.session_state.sender_process = None

if "receiver_process" not in st.session_state:
    st.session_state.receiver_process = None

# ── Nav Bar ────────────────────────────────────────────────────
# UPDATED: Links point to cleaned Streamlit URLs
st.markdown("""
<nav class="eyenet-navbar">
  <div class="brand"><span class="material-icons">radar</span>EYENET</div>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="/Overview">Overview</a>
    <a href="/Traffic_Control" class="active">Traffic Control</a>
    <a href="/Threat_Monitor">Threat Monitor</a>
    <a href="/Model_Center">Model Center</a>
  </div>
  <div class="status-pill"><span class="dot"></span>SYSTEM ONLINE</div>
</nav>
""", unsafe_allow_html=True)

# ── Page Header ────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <span class="material-icons">settings_input_antenna</span>
  <h1>Traffic Control</h1>
  <span class="page-tag">COMMAND CENTER</span>
</div>
""", unsafe_allow_html=True)
# =====================================================
# LOAD TRAFFIC DATA
# =====================================================

csv_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "radar_traffic.csv"
)

df = pd.read_csv(csv_path)

latest_status = df.iloc[-1]["status"]
latest_target = df.iloc[-1]["target_id"]
normal_count = len(df[df["status"] == "NORMAL"])

suspicious_count = len(
    df[df["status"] == "SUSPICIOUS"]
)

jamming_count = len(
    df[df["status"] == "JAMMING"]
)
# ── Status Indicators ──────────────────────────────────────────
sys_status = (
    "online"
    if st.session_state.receiver_process
    else "offline"
)
if latest_status == "JAMMING":
    net_status = "warning"

elif latest_status == "SUSPICIOUS":
    net_status = "warning"

else:
    net_status = "online"
traf_status = "online" if st.session_state.traffic_gen else "offline"

sys_label  = "ONLINE"  if sys_status  == "online"  else ("WARNING" if sys_status  == "warning" else "OFFLINE")
net_label  = "ONLINE"  if net_status  == "online"  else ("WARNING" if net_status  == "warning" else "OFFLINE")
traf_label = "ONLINE"  if traf_status == "online"  else ("WARNING" if traf_status == "warning" else "OFFLINE")

st.markdown(f"""
<div class="glass-panel">
  <h3><span class="material-icons">monitor_heart</span>SYSTEM STATUS</h3>
  <div class="status-grid">
    <div class="status-item">
      <div class="status-label">System Status</div>
      <div class="status-dot-wrapper">
        <div class="status-dot {sys_status}"></div>
        <span class="status-text {sys_status}">{sys_label}</span>
      </div>
    </div>
    <div class="status-item">
      <div class="status-label">Network Status</div>
      <div class="status-dot-wrapper">
        <div class="status-dot {net_status}"></div>
        <span class="status-text {net_status}">{net_label}</span>
      </div>
    </div>
    <div class="status-item">
      <div class="status-label">Traffic Status</div>
      <div class="status-dot-wrapper">
        <div class="status-dot {traf_status}"></div>
        <span class="status-text {traf_status}">{traf_label}</span>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
colA, colB, colC = st.columns(3)

with colA:
    st.metric(
        "Normal Packets",
        normal_count
    )

with colB:
    st.metric(
        "Suspicious Packets",
        suspicious_count
    )

with colC:
    st.metric(
        "Jamming Packets",
        jamming_count
    )
threats = suspicious_count + jamming_count

threat_rate = (
    threats / len(df)
) * 100

st.metric(
    "Threat Detection Rate",
    f"{threat_rate:.2f}%"
)

# ── Monitoring Controls ───────────────────────────────────────────
st.markdown("""<div class="glass-panel"><h3><span class="material-icons">tune</span>MONITORING CONTROLS</h3></div>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:

    if st.button("▶ Start Monitoring", use_container_width=True):

        if st.session_state.receiver_process is None:

            receiver_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "src",
                "receiver.py"
            )

            st.session_state.receiver_process = subprocess.Popen(
                ["python", receiver_path]
            )

            st.session_state.monitoring = True

            st.session_state.last_action = (
                "Receiver started successfully."
            )

        st.rerun()

      
with col2:

    if st.button("■ Stop Monitoring", use_container_width=True):

        if st.session_state.receiver_process:

            st.session_state.receiver_process.terminate()

            st.session_state.receiver_process = None

        st.session_state.monitoring = False

        st.session_state.last_action = (
            "Receiver stopped."
        )

        st.rerun()

# ── Traffic Generator Controls ─────────────────────────────────
st.markdown("""<div class="glass-panel"><h3><span class="material-icons">router</span>TRAFFIC GENERATOR</h3></div>""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:

    if st.button(
        "▶ Start Traffic Generator",
        use_container_width=True
    ):

        if st.session_state.sender_process is None:

            sender_path = os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "src",
                "sender.py"
            )

            st.session_state.sender_process = subprocess.Popen(
                ["python", sender_path]
            )

            st.session_state.traffic_gen = True

            st.session_state.last_action = (
                "Sender started successfully."
            )

        st.rerun()
with col4:

    if st.button(
        "■ Stop Traffic Generator",
        use_container_width=True
    ):

        if st.session_state.sender_process:

            st.session_state.sender_process.terminate()

            st.session_state.sender_process = None

        st.session_state.traffic_gen = False

        st.session_state.last_action = (
            "Sender stopped."
        )

        st.rerun()
# ── Scenario Injector ─────────────────────────────────────────
st.markdown("""<div class="glass-panel"><h3><span class="material-icons">bolt</span>SCENARIO INJECTOR</h3></div>""", unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
    if st.button("⚡  Inject Attack Scenario", key="attack_scen", use_container_width=True):
        st.session_state.last_action = "🔴 ATTACK ALERT: Jamming sequence injected into stream."
        st.rerun()
with col6:
    if st.button("✔  Reset to Normal", key="normal_scen", use_container_width=True):
        st.session_state.last_action = "✅ Environment cleared. Normal traffic baseline restored."
        st.rerun()

# ── Global Button Styles ──────────────────────────────────────
st.markdown("""
<style>
/* Base Streamlit Button Overrides */
div.stButton > button {
  display: flex !important; width: 100%; padding: 1.1rem !important;
  border-radius: 14px !important; font-family: 'Poppins', sans-serif !important;
  font-size: 0.88rem !important; font-weight: 600 !important;
  letter-spacing: 1px !important; text-transform: uppercase !important;
  transition: all 0.3s !important; border: 1.5px solid !important;
  background: transparent !important;
}

/* Success/Start Buttons */
div[data-testid="column"]:nth-child(1) .stButton > button { border-color: #00FFB2 !important; color: #00FFB2 !important; }
div[data-testid="column"]:nth-child(1) .stButton > button:hover { background: rgba(0,255,178,0.1) !important; box-shadow: 0 0 20px rgba(0,255,178,0.2) !important; }

/* Danger/Stop Buttons */
div[data-testid="column"]:nth-child(2) .stButton > button { border-color: #FF4D6D !important; color: #FF4D6D !important; }
div[data-testid="column"]:nth-child(2) .stButton > button:hover { background: rgba(255,77,109,0.1) !important; box-shadow: 0 0 20px rgba(255,77,109,0.2) !important; }

/* Scenario Colors Override */
div[data-testid="stVerticalBlock"] > div:nth-child(7) div[data-testid="column"]:nth-child(1) .stButton > button { border-color: #FFB84D !important; color: #FFB84D !important; }
div[data-testid="stVerticalBlock"] > div:nth-child(7) div[data-testid="column"]:nth-child(2) .stButton > button { border-color: #00E5FF !important; color: #00E5FF !important; }
</style>
""", unsafe_allow_html=True)

# ── Action Log / Console ───────────────────────────────────────
st.markdown(f"""
<div class="glass-panel">
  <h3><span class="material-icons">terminal</span>ACTION LOG</h3>
  <div style="font-family: 'Courier New', monospace; font-size: 0.85rem;
              background: rgba(0,0,0,0.3); border-radius: 10px; padding: 1.25rem;
              border: 1px solid rgba(0,229,255,0.1); color: #00E5FF; min-height: 80px;">
    <span style="color: #64748B;">[{time.strftime('%H:%M:%S')}]</span>
    &nbsp; {st.session_state.last_action}
    <span style="animation: pulse 1s infinite; display: inline-block;">█</span>
  </div>
</div>
""", unsafe_allow_html=True)




vals = df["throughput"].tail(60)
# ── Throughput Viz ───────────────────────────────────────────

fig_spark = go.Figure(go.Scatter(y=vals, mode='lines', line=dict(color='#00E5FF', width=2), fill='tozeroy', fillcolor='rgba(0,229,255,0.05)'))
fig_spark.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', xaxis=dict(visible=False), yaxis=dict(visible=False), margin=dict(l=0, r=0, t=0, b=0), height=100)

st.markdown('<div class="glass-panel"><h3><span class="material-icons">ssid_chart</span>LIVE THROUGHPUT (pkts/s)</h3>', unsafe_allow_html=True)
st.plotly_chart(fig_spark, use_container_width=True, config=dict(displayModeBar=False))
st.markdown('</div>', unsafe_allow_html=True)
st.info(
    f"Latest Target: {latest_target} | Status: {latest_status}"
)
st.markdown("### Live ML Prediction")

if latest_status == "NORMAL":

    st.success(
        f"{latest_target} classified as NORMAL"
    )

elif latest_status == "SUSPICIOUS":

    st.warning(
        f"{latest_target} classified as SUSPICIOUS"
    )

else:

    st.error(
        f"{latest_target} classified as JAMMING"
    )
st.markdown("### Recent Predictions")

st.dataframe(
    df.tail(15)[
        [
            "timestamp",
            "target_id",
            "status",
            "signal_strength",
            "latency",
            "throughput"
        ]
    ],
    use_container_width=True
)
st.markdown("""
### Model Information

- Algorithm: Random Forest
- Classes: NORMAL, SUSPICIOUS, JAMMING
- Features: 10
- Accuracy: 96.07%
""")