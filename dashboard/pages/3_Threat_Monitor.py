import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go
import random, time

# ── Page config ────────────────────────────────────────────────
st.set_page_config(page_title="EyeNet – Threat Monitor", page_icon="🛡️", layout="wide")
csv_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "data",
    "radar_traffic.csv"
)

df = pd.read_csv(csv_path)
normal_count = len(
    df[df["status"] == "NORMAL"]
)
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    unit="s"
)

suspicious_count = len(
    df[df["status"] == "SUSPICIOUS"]
)

jamming_count = len(
    df[df["status"] == "JAMMING"]
)

total = len(df)

alert_rate = round(
    ((suspicious_count + jamming_count) / total) * 100,
    2
)
# Path to CSS (Goes up one level from 'pages' to find 'style.css')
css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Nav Bar ────────────────────────────────────────────────────
# UPDATED: Links changed to match Streamlit routing (removed 1_, 2_, etc.)
st.markdown("""
<nav class="eyenet-navbar">
  <div class="brand"><span class="material-icons">radar</span>EYENET</div>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="/Overview">Overview</a>
    <a href="/Traffic_Control">Traffic Control</a>
    <a href="/Threat_Monitor" class="active">Threat Monitor</a>
    <a href="/Model_Center">Model Center</a>
  </div>
  <div class="status-pill"><span class="dot"></span>SYSTEM ONLINE</div>
</nav>
""", unsafe_allow_html=True)

# ── Page Header ────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <span class="material-icons">shield</span>
  <h1>Threat Monitor</h1>
  <span class="page-tag">SOC LIVE FEED</span>
</div>
""", unsafe_allow_html=True)

if alert_rate < 5:
    threat_level = "LOW"
elif alert_rate < 15:
    threat_level = "MEDIUM"
elif alert_rate < 30:
    threat_level = "HIGH"
else:
    threat_level = "CRITICAL"

st.markdown(f"""
<div class="glass-panel">

<h3>
THREAT LEVEL
</h3>

<h1 style="color:#FF4D6D;font-size:48px;">
{threat_level}
</h1>

<p style="color:#94A3B8;">
Alert Rate : {alert_rate}%
</p>

</div>
""", unsafe_allow_html=True)

# ── Threat Stats ───────────────────────────────────────────────
st.markdown(f"""
<div class="kpi-grid">

<div class="kpi-card danger">
<div class="kpi-label">Jamming Count</div>
<div class="kpi-value">{jamming_count}</div>
</div>

<div class="kpi-card warning">
<div class="kpi-label">Suspicious Count</div>
<div class="kpi-value">{suspicious_count}</div>
</div>

<div class="kpi-card success">
<div class="kpi-label">Normal Count</div>
<div class="kpi-value">{normal_count}</div>
</div>

<div class="kpi-card cyan">
<div class="kpi-label">Alert Rate</div>
<div class="kpi-value">{alert_rate}%</div>
</div>

</div>
""", unsafe_allow_html=True)

# ── Live Alert Feed ────────────────────────────────────────────
# ── Live Alert Feed ────────────────────────────────────────────

st.markdown("""
<div class="glass-panel">
<h3>LIVE ALERT FEED</h3>
</div>
""", unsafe_allow_html=True)

alerts_df = df[
    df["status"] != "NORMAL"
].tail(10)

st.dataframe(
    alerts_df[
        [
            "timestamp",
            "target_id",
            "status",
            "range"
        ]
    ],
    use_container_width=True
)

# ── Radar Chart and Timeline Row ───────────────────────────────
col1, col2 = st.columns([1.4, 1])

with col1:

    categories = [
        "NORMAL",
        "SUSPICIOUS",
        "JAMMING"
    ]

    values = [
        normal_count,
        suspicious_count,
        jamming_count
    ]

    values_closed = values + [values[0]]
    cats_closed = categories + [categories[0]]

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values_closed, theta=cats_closed,
        fill='toself', fillcolor='rgba(255,77,109,0.12)',
        line=dict(color='#FF4D6D', width=2),
        name='Threat Frequency',
    ))
    fig_radar.update_layout(
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            angularaxis=dict(color='#64748B', gridcolor='rgba(255,255,255,0.06)'),
            radialaxis=dict(color='#64748B', gridcolor='rgba(255,255,255,0.06)', showticklabels=False),
        ),
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Poppins', color='#E2E8F0', size=11),
        showlegend=False, margin=dict(l=30, r=30, t=20, b=20), height=300,
    )
    st.markdown('<div class="glass-panel"><h3><span class="material-icons">radar</span>THREAT DISTRIBUTION</h3>', unsafe_allow_html=True)
    st.plotly_chart(fig_radar, use_container_width=True, config=dict(displayModeBar=False))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    st.markdown("### Threat Timeline")

    st.dataframe(
        df.tail(10)[
            [
                "timestamp",
                "target_id",
                "status"
            ]
        ],
        use_container_width=True
    )

latest = df.iloc[-1]

st.markdown("## Latest ML Prediction")

if latest["status"] == "NORMAL":

    st.success(
        f'{latest["target_id"]} classified as NORMAL'
    )

elif latest["status"] == "SUSPICIOUS":

    st.warning(
        f'{latest["target_id"]} classified as SUSPICIOUS'
    )

else:

    st.error(
        f'{latest["target_id"]} classified as JAMMING'
    )