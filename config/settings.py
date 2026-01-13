"""
Configuration file for Smart Energy Monitoring System

IMPORTANT:
- No API keys are hardcoded here
- All sensitive values are loaded from environment variables
- This file is SAFE to push to GitHub
"""

import os

# ================== THINGSPEAK CONFIG ==================

# ThingSpeak base URL
THINGSPEAK_URL = "https://api.thingspeak.com/update"

# Read API key from environment variable (SAFE)
THINGSPEAK_API_KEY = os.getenv("THINGSPEAK_API_KEY")

# ================== SYSTEM CONFIG ==================

# Time interval (in seconds) between readings
TIME_INTERVAL = 5

# Electricity unit cost (₹ per kWh)
UNIT_COST = 6.5

# Default power threshold (Watts)
DEFAULT_POWER_THRESHOLD = 1000
