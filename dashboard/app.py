import streamlit as st
import os

# ── Page config ────────────────────────────────────────────────
st.set_page_config(
    page_title="EyeNet – AI Radar Monitor",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed", # Hides default sidebar for a cleaner look
)

# ── Inject CSS ─────────────────────────────────────────────────
# Ensures the futuristic SOC theme is applied
css_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error("style.css not found. Please ensure it is in the same folder as app.py")

# ── Top Navigation Bar ─────────────────────────────────────────
# Updated to point to Streamlit's "cleaned" URLs (no numbers)
st.markdown("""
<nav class="eyenet-navbar">
  <div class="brand">
    <span class="material-icons">radar</span>
    EYENET
  </div>
  <div class="nav-links">
    <a href="/" class="active">Home</a>
    <a href="/Overview">Overview</a>
    <a href="/Traffic_Control">Traffic Control</a>
    <a href="/Threat_Monitor">Threat Monitor</a>
    <a href="/Model_Center">Model Center</a>
  </div>
  <div class="status-pill">
    <span class="dot"></span>
    SYSTEM ONLINE
  </div>
</nav>
""", unsafe_allow_html=True)

# ── Hero Section ───────────────────────────────────────────────
st.markdown("""
<section class="hero-section">
  <div class="radar-logo-wrapper">
    <div class="radar-rings">
      <div class="radar-ring"></div>
      <div class="radar-ring"></div>
      <div class="radar-ring"></div>
    </div>
    <div class="radar-icon-center">
      <span class="material-icons">radar</span>
    </div>
  </div>
  <h1 class="hero-title">EyeNet</h1>
  <p class="hero-subtitle">AI Radar Communication Monitoring System</p>
</section>
""", unsafe_allow_html=True)

# ── Navigation Cards ───────────────────────────────────────────
# Updated href attributes to match Streamlit's internal routing
st.markdown("""
<div class="nav-cards-grid">

  <a class="nav-card" href="/Overview">
    <div class="card-icon">
      <span class="material-icons">dashboard</span>
    </div>
    <div class="card-title">Overview</div>
    <div class="card-desc">
      System metrics, analytics, network health and communication statistics.
    </div>
    <div class="card-arrow">
      <span class="material-icons">arrow_forward</span>
    </div>
  </a>

  <a class="nav-card" href="/Traffic_Control">
    <div class="card-icon">
      <span class="material-icons">settings_input_antenna</span>
    </div>
    <div class="card-title">Traffic Control</div>
    <div class="card-desc">
      Manage traffic generation, monitoring services and simulations.
    </div>
    <div class="card-arrow">
      <span class="material-icons">arrow_forward</span>
    </div>
  </a>

  <a class="nav-card" href="/Threat_Monitor">
    <div class="card-icon">
      <span class="material-icons">shield</span>
    </div>
    <div class="card-title">Threat Monitor</div>
    <div class="card-desc">
      Monitor jamming attacks, suspicious traffic and security alerts.
    </div>
    <div class="card-arrow">
      <span class="material-icons">arrow_forward</span>
    </div>
  </a>

  <a class="nav-card" href="/Model_Center">
    <div class="card-icon">
      <span class="material-icons">memory</span>
    </div>
    <div class="card-title">Model Center</div>
    <div class="card-desc">
      Train, evaluate and manage machine learning models.
    </div>
    <div class="card-arrow">
      <span class="material-icons">arrow_forward</span>
    </div>
  </a>

</div>
""", unsafe_allow_html=True)

# ── Footer spacer ──────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)