import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Energy Dashboard",
    page_icon="⚡",
    layout="wide"
)

# ---------------- SIDEBAR (CONTROLS) ----------------
st.sidebar.title("⚙️ Controls")

power_threshold = st.sidebar.number_input(
    "High Power Threshold (W)",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)

filter_option = st.sidebar.selectbox(
    "Filter data",
    ["All data", "Last 10 minutes", "Last 30 minutes", "Last 1 hour"]
)

# ---------------- TITLE ----------------
st.title("⚡ Smart Energy Monitoring System")
st.caption("Professional IoT Energy Dashboard")

DATA_FILE = "data/energy_log.csv"

# ---------------- LOAD DATA ----------------
df = pd.read_csv(DATA_FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

# ---------------- APPLY FILTER ----------------
now = datetime.now()

if filter_option == "Last 10 minutes":
    df = df[df["timestamp"] >= now - timedelta(minutes=10)]
elif filter_option == "Last 30 minutes":
    df = df[df["timestamp"] >= now - timedelta(minutes=30)]
elif filter_option == "Last 1 hour":
    df = df[df["timestamp"] >= now - timedelta(hours=1)]
# else: All data → no filtering

latest = df.iloc[-1]
total_energy = df["energy"].sum()
estimated_bill = round(total_energy * 6.5, 2)

# ---------------- METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Voltage (V)", round(latest["voltage"], 2))
col2.metric("Current (A)", round(latest["current"], 2))
col3.metric("Power (W)", round(latest["power"], 2))
col4.metric("Energy (kWh)", round(total_energy, 4))

# ---------------- ALERT ----------------
st.subheader("🚦 System Status")

if latest["power"] > power_threshold:
    st.error("🚨 HIGH ENERGY CONSUMPTION DETECTED")
else:
    st.success("✅ ENERGY CONSUMPTION NORMAL")

# ---------------- CHARTS ----------------
st.subheader("📈 Power Consumption Over Time")
st.line_chart(df.set_index("timestamp")["power"])

st.subheader("📉 Energy Consumption Over Time")
st.area_chart(df.set_index("timestamp")["energy"])

# ---------------- REPORT ----------------
st.subheader("📄 Energy Usage Report")
st.write(df.describe())

st.download_button(
    "⬇️ Download CSV Report",
    df.to_csv(index=False),
    "energy_report.csv",
    "text/csv"
)
