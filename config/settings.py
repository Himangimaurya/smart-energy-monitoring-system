"""
settings.py
-------------
This file contains all configuration values used across the project.
"""

# Electricity unit cost (₹ per kWh)
UNIT_COST = 6.5

# Power threshold in Watts (above this is considered high usage)
POWER_THRESHOLD = 1000

# Time interval for simulation (seconds)
TIME_INTERVAL = 2

# ThingSpeak cloud configuration
THINGSPEAK_API_KEY = "WXCC5E64JNB78J6V"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
