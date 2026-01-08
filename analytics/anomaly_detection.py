from config.settings import POWER_THRESHOLD


class AnomalyDetector:
    def is_high_consumption(self, power):
        """
        Check if power exceeds threshold
        """
        if power > POWER_THRESHOLD:
            return True
        return False
