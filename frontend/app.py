import os
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta

# ----------------------------------------
# Page Config
# ----------------------------------------
st.set_page_config(
    page_title="Smart Energy Monitoring System",
    page_icon="⚡",
    layout="wide"
)

# ----------------------------------------
# Title
# ----------------------------------------
st.markdown("## ⚡ Smart Energy Monitoring System")
st.caption("Professional IoT Energy Dashboard")

# ----------------------------------------
# Data file path
# ----------------------------------------
DATA_FILE = "data/energy_log.csv"

# ----------------------------------------
# Load or Generate Data
# ----------------------------------------
def load_energy_data():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        if df.empty:
            return generate_demo_data()
        return df
    else:
        return generate_demo_data()

def generate_demo_data():
    timestamps = [
        datetime.now() - timedelta(minutes=i)
        for i in range(50, 0, -1)
    ]

    voltage = np.random.normal(230, 5, 50)
    current = np.random.normal(5, 1.5, 50)
    power = voltage * current
    energy = np.cumsum(power) / 3600000  # kWh

    return pd.DataFrame({
        "timestamp": timestamps,
        "voltage": voltage,
        "current": current,
        "power": power,
        "energy": energy
    })

# ----------------------------------------
# Load data
# ----------------------------------------
df = load_energy_data()

# ----------------------------------------
# Sidebar Controls
# ----------------------------------------
st.sidebar.header("⚙ Controls")

power_threshold = st.sidebar.slider(
    "High Power Threshold (W)",
    min_value=500,
    max_value=5000,
    value=2000,
    step=100
)

# ----------------------------------------
# Latest Values
# ----------------------------------------
latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Voltage (V)", f"{latest['voltage']:.2f}")
col2.metric("Current (A)", f"{latest['current']:.2f}")
col3.metric("Power (W)", f"{latest['power']:.2f}")
col4.metric("Energy (kWh)", f"{latest['energy']:.4f}")

# ----------------------------------------
# Alert
# ----------------------------------------
if latest["power"] > power_threshold:
    st.error("🚨 HIGH ENERGY CONSUMPTION DETECTED")
else:
    st.success("✅ Energy consumption is normal")

# ----------------------------------------
# Charts
# ----------------------------------------
st.subheader("📊 Energy Trends")

colA, colB = st.columns(2)

with colA:
    st.line_chart(df.set_index("timestamp")["power"])

with colB:
    st.line_chart(df.set_index("timestamp")["energy"])

# ----------------------------------------
# Footer
# ----------------------------------------
st.info("Dashboard running successfully (demo data mode)")

    