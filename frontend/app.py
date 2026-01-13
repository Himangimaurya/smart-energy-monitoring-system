import os
import pandas as pd
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Smart Energy Monitoring System",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# CONSTANTS
# --------------------------------------------------
DATA_FILE = "data/energy_log.csv"

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    """
    <h1>⚡ Smart Energy Monitoring System</h1>
    <p style="color: gray;">Professional IoT Energy Dashboard</p>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIDEBAR CONTROLS
# --------------------------------------------------
st.sidebar.header("⚙️ Controls")

power_threshold = st.sidebar.number_input(
    "High Power Threshold (W)",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)

filter_option = st.sidebar.selectbox(
    "Filter data",
    ["All data", "Last 10 records", "Last 50 records"]
)

# --------------------------------------------------
# LOAD DATA SAFELY (CLOUD SAFE)
# --------------------------------------------------
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    st.warning("No energy data found yet. Please run the backend to generate data.")
    df = pd.DataFrame(
        columns=["timestamp", "voltage", "current", "power", "energy"]
    )

# --------------------------------------------------
# HANDLE EMPTY DATA
# --------------------------------------------------
if df.empty:
    st.info("Dashboard is ready. Waiting for energy data...")
    st.stop()

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------
if filter_option == "Last 10 records":
    df = df.tail(10)
elif filter_option == "Last 50 records":
    df = df.tail(50)

# --------------------------------------------------
# LATEST VALUES
# --------------------------------------------------
latest = df.iloc[-1]
total_energy = df["energy"].sum()

# --------------------------------------------------
# METRICS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Voltage (V)", round(float(latest["voltage"]), 2))
col2.metric("Current (A)", round(float(latest["current"]), 2))
col3.metric("Power (W)", round(float(latest["power"]), 2))
col4.metric("Energy (kWh)", round(float(total_energy), 4))

# --------------------------
