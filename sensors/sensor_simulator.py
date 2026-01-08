import random

class SensorSimulator:
    def get_voltage(self):
        # Simulate voltage between 210V–240V
        return round(random.uniform(210, 240), 2)

    def get_current(self):
        # Simulate current between 1A–10A
        return round(random.uniform(1, 10), 2)
