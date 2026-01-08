# ⚡ Smart Energy Monitoring System (Software-Based IoT Project)

## 📌 Project Overview

The **Smart Energy Monitoring System** is a **software-only IoT project** developed using **Python**.  
It simulates electrical sensors to monitor **voltage, current, power, and energy consumption**, stores the data, uploads it to the cloud, and displays it using a **live interactive dashboard**.

👉 No physical hardware is required.  
👉 All data is generated using Python simulation.

---

## 🎯 Project Objective

The main objectives of this project are:

- Simulate electrical sensor data (Voltage and Current)
- Calculate power (W) and energy consumption (kWh)
- Track energy usage over time
- Detect high or abnormal energy consumption
- Predict electricity bill
- Upload data to an IoT cloud platform (ThingSpeak)
- Visualize data using a frontend dashboard

---

## 🧠 How the Project Works

1. **Sensor Simulation**
   - Voltage and current values are generated using Python
   - Values represent real household electrical readings

2. **Energy Calculation**
   - Power is calculated using:  
     `Power = Voltage × Current`
   - Energy is calculated in kWh based on time

3. **Data Logging**
   - All calculated values are saved in a CSV file (`energy_log.csv`)

4. **Anomaly Detection**
   - If power crosses a defined threshold, the system raises an alert

5. **Bill Prediction**
   - Energy consumption is used to estimate electricity cost

6. **Cloud Upload**
   - Power and energy data are uploaded to ThingSpeak using its API

7. **Frontend Dashboard**
   - A Streamlit-based dashboard displays live data, alerts, charts, and reports

---

## 🏗️ Project Architecture

