import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import random, math

# ── Page config ────────────────────────────────────────────────
st.set_page_config(page_title="EyeNet – Overview", page_icon="📊", layout="wide")

# Path to CSS (Goes up one level from 'pages' to find 'style.css')
css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# LOAD REAL RADAR DATA
# =====================================================

BASE_DIR = os.path.dirname(__file__)

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "data",
    "radar_traffic.csv"
)

df = pd.read_csv(csv_path)

total_packets = len(df)

normal_count = len(
    df[df["status"] == "NORMAL"]
)

suspicious_count = len(
    df[df["status"] == "SUSPICIOUS"]
)

jamming_count = len(
    df[df["status"] == "JAMMING"]
)

# ── Nav Bar ────────────────────────────────────────────────────
# UPDATED: Links changed to match Streamlit routing (no 1_, 2_, etc.)
st.markdown("""
<nav class="eyenet-navbar">
  <div class="brand"><span class="material-icons">radar</span>EYENET</div>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="/Overview" class="active">Overview</a>
    <a href="/Traffic_Control">Traffic Control</a>
    <a href="/Threat_Monitor">Threat Monitor</a>
    <a href="/Model_Center">Model Center</a>
  </div>
  <div class="status-pill"><span class="dot"></span>SYSTEM ONLINE</div>
</nav>
""", unsafe_allow_html=True)

# ── Page Header ────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <span class="material-icons">dashboard</span>
  <h1>Overview</h1>
  <span class="page-tag">LIVE ANALYTICS</span>
</div>
""", unsafe_allow_html=True)

# ── KPI Cards ─────────────────────────────────────────────────

st.markdown(f"""
<div class="kpi-grid">

  <div class="kpi-card cyan">
    <span class="material-icons kpi-icon">analytics</span>
    <div class="kpi-label">Total Packets Processed</div>
    <div class="kpi-value">{total_packets}</div>
  </div>

  <div class="kpi-card success">
    <span class="material-icons kpi-icon">check_circle</span>
    <div class="kpi-label">Normal Traffic</div>
    <div class="kpi-value">{normal_count}</div>
  </div>

  <div class="kpi-card danger">
    <span class="material-icons kpi-icon">warning</span>
    <div class="kpi-label">Jamming Alerts</div>
    <div class="kpi-value">{jamming_count}</div>
  </div>

  <div class="kpi-card warning">
    <span class="material-icons kpi-icon">security</span>
    <div class="kpi-label">Suspicious Activities</div>
    <div class="kpi-value">{suspicious_count}</div>
  </div>

</div>
""", unsafe_allow_html=True)
st.markdown(f"""
<div class="glass-panel">

<h3>
<span class="material-icons">
psychology
</span>
MODEL PERFORMANCE
</h3>

<h1 style="
color:#00E5FF;
margin-top:10px;
font-size:48px;
">
96.07%
</h1>

<p style="color:#94A3B8;">
Random Forest Accuracy
</p>

</div>
""", unsafe_allow_html=True)
# ── Traffic Analytics Chart ────────────────────────────────────
recent = df.tail(300)

normal = []
suspicious = []
jamming = []

for i in range(1, len(recent) + 1):

    temp = recent.iloc[:i]

    normal.append(
        len(temp[temp["status"] == "NORMAL"])
    )

    suspicious.append(
        len(temp[temp["status"] == "SUSPICIOUS"])
    )

    jamming.append(
        len(temp[temp["status"] == "JAMMING"])
    )

hours = list(range(len(recent)))

fig_traffic = go.Figure()
fig_traffic.add_trace(go.Scatter(
    x=hours, y=normal, name="Normal Traffic",
    fill='tozeroy', line=dict(color='#00E5FF', width=2),
    fillcolor='rgba(0,229,255,0.08)'
))
fig_traffic.add_trace(go.Scatter(
    x=hours, y=suspicious, name="Suspicious Traffic",
    fill='tozeroy', line=dict(color='#FFB84D', width=2),
    fillcolor='rgba(255,184,77,0.08)'
))
fig_traffic.add_trace(go.Scatter(
    x=hours, y=jamming, name="Jamming Traffic",
    fill='tozeroy', line=dict(color='#FF4D6D', width=2),
    fillcolor='rgba(255,77,109,0.08)'
))
fig_traffic.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Poppins', color='#64748B', size=11),
    title=dict(text='24-Hour Traffic Analytics', font=dict(color='#E2E8F0', size=13)),
    legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#E2E8F0')),
    xaxis=dict(gridcolor='rgba(255,255,255,0.04)', color='#64748B'),
    yaxis=dict(gridcolor='rgba(255,255,255,0.04)', color='#64748B'),
    margin=dict(l=10, r=10, t=40, b=10),
    height=320,
)

st.markdown('<div class="glass-panel"><h3><span class="material-icons">show_chart</span>TRAFFIC ANALYTICS</h3>', unsafe_allow_html=True)
st.plotly_chart(fig_traffic, use_container_width=True, config=dict(displayModeBar=False))
st.markdown('</div>', unsafe_allow_html=True)

# ── Secondary Row ──────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

with col1:
    fig_donut = go.Figure(data=[go.Pie(
        labels=['Normal', 'Suspicious', 'Jamming'],
        values=[
    normal_count,
    suspicious_count,
    jamming_count
],
        hole=0.6,
        marker=dict(colors=['#00FFB2', '#FFB84D', '#FF4D6D'],
                    line=dict(color='#141B34', width=2)),
        textfont=dict(family='Poppins', color='#E2E8F0'),
        hoverinfo='label+percent',
    )])
    fig_donut.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#E2E8F0', family='Poppins')),
        font=dict(family='Poppins'),
        annotations=[dict(text='Threat<br>Distribution', x=0.5, y=0.5,
                          font=dict(size=12, color='#E2E8F0', family='Poppins'),
                          showarrow=False)],
        margin=dict(l=10, r=10, t=10, b=10),
        height=300,
    )
    st.markdown('<div class="glass-panel"><h3><span class="material-icons">donut_large</span>THREAT DISTRIBUTION</h3>', unsafe_allow_html=True)
    st.plotly_chart(fig_donut, use_container_width=True, config=dict(displayModeBar=False))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:

    features = [
        "packet_rate",
        "latency",
        "packet_loss",
        "velocity",
        "throughput",
        "signal_latency_ratio",
        "network_health_score",
        "packet_size",
        "signal_strength",
        "range"
    ]

    importance = [
        0.1963,
        0.1874,
        0.1288,
        0.1023,
        0.1016,
        0.0998,
        0.0654,
        0.0549,
        0.0466,
        0.0168
    ]

    fig_feat = go.Figure(go.Bar(
        x=importance,
        y=features,
        orientation='h',
        marker=dict(
            color=importance,
            colorscale=[[0, '#A855F7'], [1, '#00E5FF']],
            line=dict(width=0),
        ),
        text=[f"{v:.0%}" for v in importance],
        textposition='outside',
        textfont=dict(color='#E2E8F0', family='Poppins', size=11),
    ))

    fig_feat.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Poppins', color='#64748B'),
        xaxis=dict(visible=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.04)', color='#E2E8F0'),
        margin=dict(l=10, r=60, t=10, b=10),
        height=300,
    )

    st.markdown(
        '<div class="glass-panel"><h3><span class="material-icons">bar_chart</span>FEATURE IMPORTANCE</h3>',
        unsafe_allow_html=True
    )

    st.plotly_chart(
        fig_feat,
        use_container_width=True,
        config=dict(displayModeBar=False)
    )

    st.markdown('</div>', unsafe_allow_html=True)
normal_pct = 0
suspicious_pct = 0
jamming_pct = 0

if total_packets > 0:
    normal_pct = round(normal_count / total_packets * 100, 2)
    suspicious_pct = round(suspicious_count / total_packets * 100, 2)
    jamming_pct = round(jamming_count / total_packets * 100, 2)
colA,colB,colC = st.columns(3)

with colA:
    st.metric(
        "Normal %",
       normal_pct
    )

with colB:
    st.metric(
        "Suspicious %",
        suspicious_pct
    )

with colC:
    st.metric(
        "Jamming %",
       jamming_pct
    )
st.markdown(f"""
<div class="glass-panel">

<h3>
<span class="material-icons">
memory
</span>
MODEL SUMMARY
</h3>

<ul style="color:white;">
<li>Algorithm: Random Forest</li>
<li>Accuracy: 96.07%</li>
<li>Classes: NORMAL, SUSPICIOUS, JAMMING</li>
<li>Training Samples: {total_packets}</li>
<li>Features Used: 10</li>
</ul>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="glass-panel">
<h3>
<span class="material-icons">
list_alt
</span>
RECENT ACTIVITY
</h3>
</div>
""", unsafe_allow_html=True)

recent = df.tail(10)

st.dataframe(
    recent[
        [
            "timestamp",
            "target_id",
            "status",
            "signal_strength",
            "packet_loss",
            "latency"
        ]
    ],
    use_container_width=True
)