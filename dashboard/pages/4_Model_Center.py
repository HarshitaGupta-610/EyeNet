import streamlit as st
import os
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="EyeNet – Model Center",
    page_icon="🧠",
    layout="wide"
)

# --- CSS LOADING ---
css_path = os.path.join(os.path.dirname(__file__), "..", "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- DATASET LOADING ---
csv_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "radar_traffic.csv")

try:
    df = pd.read_csv(csv_path)
    total_records = len(df)
    normal_count = len(df[df["status"] == "NORMAL"])
    suspicious_count = len(df[df["status"] == "SUSPICIOUS"])
    jamming_count = len(df[df["status"] == "JAMMING"])
except Exception:
    df = pd.DataFrame()
    total_records, normal_count, suspicious_count, jamming_count = 0, 0, 0, 0

# --- NAVBAR ---
st.markdown("""
<nav class="eyenet-navbar">
  <div class="brand">
    <span class="material-icons">radar</span>
    EYENET
  </div>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="/Overview">Overview</a>
    <a href="/Traffic_Control">Traffic Control</a>
    <a href="/Threat_Monitor">Threat Monitor</a>
    <a href="/Model_Center" class="active">Model Center</a>
  </div>
  <div class="status-pill">
    <span class="dot"></span>
    SYSTEM ONLINE
  </div>
</nav>
""", unsafe_allow_html=True)

# --- PAGE HEADER ---
st.markdown("""
<div class="page-header">
  <span class="material-icons">memory</span>
  <h1>Model Center</h1>
  <span class="page-tag">AI ANALYTICS</span>
</div>
""", unsafe_allow_html=True)

# --- HOW EYENET WORKS ---
st.markdown("""
<div class="glass-panel" style="border-left:4px solid #00E5FF; background:rgba(0,229,255,0.04);">
<h3>🧠 HOW EYENET WORKS</h3>
<p style="line-height:1.9;">
<b>Traffic Control Page</b><br>
Simulates radar communication and generates live traffic data. It also monitors incoming traffic and allows testing of attack scenarios.
<br><br>
<b>Threat Monitor Page</b><br>
Displays all detected threats in real time. The system identifies whether incoming traffic is normal, suspicious, or a possible jamming attack.
<br><br>
<b>Model Center Page</b><br>
Provides information about the Artificial Intelligence model, the dataset being analyzed, prediction statistics, and the latest decisions made by the AI system.
<br><br>
<b>Project Workflow</b><br>

Traffic Generation
➡️ Packet Reception
➡️ Feature Extraction
➡️ Random Forest Prediction
➡️ Alert Generation
➡️ Threat Monitoring

</p>
</div>
""", unsafe_allow_html=True)

# --- ACTIVE MODEL CARD ---
st.markdown(f"""
<div class="glass-panel">
<h3>ACTIVE MODEL</h3>
<h2 style="color:#00E5FF;">
Random Forest Classifier
</h2>
<p>
Machine Learning model trained to classify radar communication traffic into Normal, Suspicious, and Jamming categories.
</p>
<ul>
<li>Input Features : 10</li>
<li>Output Classes : NORMAL, SUSPICIOUS, JAMMING</li>
<li>Current Dataset Records : {total_records}</li>
</ul>
<p style="color:#00FFB2;">
🟢 MODEL ONLINE
</p>
</div>
""", unsafe_allow_html=True)

# --- DATA USED BY THE MODEL ---
st.markdown(f"""
<div class="glass-panel">
<h3>📊 DATA USED BY THE MODEL</h3>
<p>The following features are extracted from radar signals and fed into the Random Forest model for classification:</p>
<ul style="column-count: 2;">
<li>Signal Strength</li>
<li>Packet Rate</li>
<li>Latency</li>
<li>Packet Loss</li>
<li>Throughput</li>
<li>Velocity</li>
<li>Network Health Score</li>
<li>Signal Latency Ratio</li>
<li>Packet Size</li>
<li>Range</li>
</ul>
</div>
""", unsafe_allow_html=True)

# --- LIVE DATASET STATISTICS ---
st.markdown("## Live Dataset Statistics")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Total Records", total_records)
with c2:
    st.metric("Normal", normal_count)
with c3:
    st.metric("Suspicious", suspicious_count)
with c4:
    st.metric("Jamming", jamming_count)

# --- TRAFFIC DISTRIBUTION GRAPH ---
fig = go.Figure()
fig.add_bar(
    x=["NORMAL", "SUSPICIOUS", "JAMMING"],
    y=[normal_count, suspicious_count, jamming_count],
    marker_color=['#00FFB2', '#FFC107', '#FF5252']
)
fig.update_layout(
    title="Traffic Distribution (Based on ML Predictions)",
    height=400,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)

# --- MODEL INFORMATION ---
st.markdown("""
<div class="glass-panel">
<h3>📘 MODEL INFORMATION</h3>
<p style="line-height:1.9;">
<b>Algorithm Used:</b>
Random Forest Classifier
<br><br>
<b>Purpose:</b>
Detect abnormal radar communication behaviour.
<br><br>
<b>Possible Outputs:</b>
<ul>
<li>NORMAL → Communication is healthy</li>
<li>SUSPICIOUS → Unusual behaviour detected</li>
<li>JAMMING → Possible attack detected</li>
</ul>
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-panel">

<h3>📊 Features Analysed By The AI Model</h3>

<p style="line-height:1.8;">

Before making a prediction, the Random Forest model analyses the following network parameters:

• Signal Strength<br>
• Packet Rate<br>
• Latency<br>
• Packet Loss<br>
• Throughput<br>
• Velocity<br>
• Network Health Score<br>
• Signal Latency Ratio<br>
• Packet Size<br>
• Range

</p>

</div>
""", unsafe_allow_html=True)

# --- LATEST ML PREDICTION ---
st.markdown("## Latest ML Prediction")

if not df.empty:
    latest = df.iloc[-1]
    
    prediction_text = f"""
    Target ID : {latest.get("target_id", "N/A")}
    
    Status : {latest.get("status", "N/A")}
    
    Signal Strength : {latest.get("signal_strength", "N/A")}
    
    Latency : {latest.get("latency", "N/A")}
    
    Packet Loss : {latest.get("packet_loss", "N/A")}
    
    Throughput : {latest.get("throughput", "N/A")}
    """

    status = latest.get("status", "NORMAL")
    if status == "NORMAL":
        st.success(prediction_text)
    elif status == "SUSPICIOUS":
        st.warning(prediction_text)
    else:
        st.error(prediction_text)
else:
    st.info("No data available yet. Please generate traffic in the Traffic Control page.")
st.markdown("""
<div class="glass-panel">

<h3>🚨 ALERT SYSTEM</h3>

<p style="line-height:1.8;">

Whenever the AI model predicts
<b>SUSPICIOUS</b> or <b>JAMMING</b> activity,
EyeNet automatically generates an alert.

The alert contains:

• Target ID<br>
• Signal Strength<br>
• Packet Loss<br>
• Latency<br>
• Timestamp

These alerts help operators quickly identify
potential threats and monitor abnormal activity.

</p>

</div>
""", unsafe_allow_html=True)
# --- SYSTEM SUMMARY ---
st.markdown("""
<div class="glass-panel">
<h3>📡 SYSTEM SUMMARY</h3>
This page represents the Machine Learning engine of EyeNet. 
The Random Forest model receives radar communication data, 
analyzes network behaviour using 10 extracted features, 
and classifies each communication event as NORMAL, SUSPICIOUS, or JAMMING.
<br><br>
The resulting predictions are stored in the dataset and 
displayed on the Traffic Control and Threat Monitor pages 
for real-time monitoring and defensive action.
</div>
""", unsafe_allow_html=True)