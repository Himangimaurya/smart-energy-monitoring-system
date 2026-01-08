from sensors.sensor_simulator import SensorSimulator
from energy.energy_calculator import EnergyCalculator

sensor = SensorSimulator()
calculator = EnergyCalculator()

voltage = sensor.get_voltage()
current = sensor.get_current()

power = calculator.calculate_power(voltage, current)
energy = calculator.calculate_energy(power, time_hours=1)

print(f"Voltage : {voltage} V")
print(f"Current : {current} A")
print(f"Power   : {power} W")
print(f"Energy  : {energy} kWh (for 1 hour)")
