class EnergyCalculator:
    def calculate_power(self, voltage, current):
        """
        Calculate power in Watts
        P = V × I
        """
        return round(voltage * current, 2)

    def calculate_energy(self, power, time_hours):
        """
        Calculate energy in kWh
        Energy = (Power × Time) / 1000
        """
        return round((power * time_hours) / 1000, 4)



