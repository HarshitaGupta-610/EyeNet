# 🛡️ EyeNet – AI Powered Radar Threat Detection System

## 📌 Project Overview

EyeNet is an Artificial Intelligence based radar monitoring system designed to detect abnormal communication behavior and potential jamming attacks in radar networks.

The project simulates radar communication traffic, analyzes network behavior using Machine Learning, and classifies incoming traffic into different threat categories.

EyeNet provides a real-time dashboard that allows users to monitor communication activity, view detected threats, and understand how the AI model makes decisions.

---

# 🤔 Why Was This Project Created?

Modern radar systems continuously exchange huge amounts of communication data.

Monitoring all this information manually is difficult because:

* Thousands of communication events can occur every minute.
* Human operators may miss unusual patterns.
* Threats need to be detected quickly.
* Jamming attacks can disrupt communication systems.

To solve this problem, EyeNet uses Artificial Intelligence to automatically analyze communication behavior and identify suspicious activity.

---

# 📡 What is Radar?

Radar stands for:

**R**adio
**D**etection
**A**nd
**R**anging

A radar system sends radio waves into the environment.

When these waves hit an object, they bounce back to the radar receiver.

Using the returned signals, radar systems can estimate:

* Distance of an object
* Direction of an object
* Speed of an object
* Position of an object

Radar technology is widely used in:

* Airports
* Aircraft systems
* Ships
* Defense systems
* Drone detection systems
* Weather monitoring systems

---

# 🚨 What Threats Can Occur?

Radar communication systems may experience different types of communication behavior.

## ✅ NORMAL

Communication is operating correctly.

Characteristics:

* Stable signal quality
* Low packet loss
* Healthy network conditions
* Normal traffic patterns

---

## ⚠️ SUSPICIOUS

Communication appears unusual.

Examples:

* Unexpected traffic spikes
* Abnormal latency
* Increased packet loss
* Unusual communication behavior

Suspicious traffic may indicate a developing issue or possible attack.

---

## 🚫 JAMMING

Jamming occurs when unwanted signals interfere with communication.

Effects include:

* Reduced communication quality
* Signal degradation
* Loss of communication
* Incorrect radar information

Jamming attacks are considered serious threats and require immediate attention.

---

# 🧠 Why Use Artificial Intelligence?

Without AI, every communication event would need to be inspected manually.

This becomes difficult when large volumes of data are generated continuously.

The AI system can:

* Analyze communication patterns automatically
* Detect unusual behavior quickly
* Classify traffic in real time
* Reduce human workload
* Improve threat detection speed

---

# ⚙️ How EyeNet Works

The complete workflow is shown below:

Radar Traffic Generation

⬇

Data Collection

⬇

Feature Extraction

⬇

Machine Learning Analysis

⬇

Threat Classification

⬇

Real-Time Monitoring

---

## Step 1: Traffic Generation

The system generates simulated radar communication traffic.

Each communication event contains information such as:

* Signal Strength
* Latency
* Packet Loss
* Throughput
* Packet Rate
* Velocity
* Network Health Score
* Range

---

## Step 2: Data Collection

Generated traffic is collected and stored.

This data becomes the input for the Machine Learning model.

---

## Step 3: Feature Analysis

The AI model analyzes communication characteristics including:

* Signal Strength
* Packet Rate
* Latency
* Packet Loss
* Throughput
* Velocity
* Packet Size
* Range
* Network Health Score
* Signal Latency Ratio

These features help the model understand whether communication behavior is normal or abnormal.

---

## Step 4: Machine Learning Prediction

A Random Forest Classifier processes the extracted features.

The model predicts one of three classes:

* NORMAL
* SUSPICIOUS
* JAMMING

---

## Step 5: Threat Monitoring

The prediction results are displayed on the dashboard.

Users can monitor:

* Live traffic
* Active threats
* Alert statistics
* Threat trends

in real time.

---

# 🧩 Dashboard Pages

## 🏠 Home Page

The landing page of the application.

Displays:

* Project introduction
* System status
* Navigation to all modules

---

## 📊 Overview Page

Provides a high-level summary of system activity.

Displays:

* Total communication records
* Threat statistics
* Overall network information
* System overview charts

---

## 📡 Traffic Control Page

Acts as the communication simulation center.

Features:

* Radar traffic generation
* Communication monitoring
* Live packet activity
* Traffic visualization

This page is responsible for producing the data used throughout the project.

---

## 🚨 Threat Monitor Page

Acts as the Security Operations Center (SOC).

Features:

* Live threat feed
* Threat statistics
* Alert monitoring
* Threat timeline
* Threat distribution visualization

This page displays the threats detected by the AI model.

---

## 🧠 Model Center Page

Represents the Artificial Intelligence engine of EyeNet.

Features:

* Machine Learning model information
* Dataset statistics
* AI workflow explanation
* Input features used by the model
* Latest prediction generated by AI

This page helps users understand how the AI system works.

---

# 📂 Dataset

The project uses a dataset containing radar communication information.

Example fields include:

| Feature              | Description                     |
| -------------------- | ------------------------------- |
| target_id            | Communication target identifier |
| range                | Distance measurement            |
| velocity             | Speed information               |
| signal_strength      | Signal quality                  |
| latency              | Communication delay             |
| packet_loss          | Lost packets percentage         |
| throughput           | Data transfer rate              |
| packet_rate          | Packet transmission frequency   |
| network_health_score | Network condition indicator     |
| signal_latency_ratio | Signal performance metric       |
| status               | Predicted traffic category      |

---

# 🤖 Machine Learning Model

Algorithm Used:

**Random Forest Classifier**

Why Random Forest?

* Easy to interpret
* Handles multiple features effectively
* Good classification performance
* Robust against noisy data
* Suitable for threat detection tasks

Output Classes:

* NORMAL
* SUSPICIOUS
* JAMMING

---

# 🛠️ Technologies Used

### Frontend

* Streamlit

### Data Processing

* Pandas

### Visualization

* Plotly

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Programming Language

* Python

---

# 🎯 Project Objective

The primary objective of EyeNet is to demonstrate how Artificial Intelligence can be used to monitor radar communication systems and automatically detect abnormal communication behavior.

The system helps transform raw communication data into actionable threat information that can be monitored in real time.

---

# 👨‍💻 Developed By

EyeNet – AI Powered Radar Threat Detection System

Academic / Research Project

Built using Python, Streamlit, and Machine Learning.
