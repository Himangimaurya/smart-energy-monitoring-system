import csv
import os
import time


class EnergyLogger:
    def __init__(self, file_path="data/energy_log.csv"):
        self.file_path = file_path
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self):
        """
        Create CSV file with headers if it does not exist
        """
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "timestamp",
                    "voltage",
                    "current",
                    "power",
                    "energy"
                ])

    def log(self, voltage, current, power, energy):
        """
        Log one row of energy data
        """
        with open(self.file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                time.strftime("%Y-%m-%d %H:%M:%S"),
                voltage,
                current,
                power,
                energy
            ])
