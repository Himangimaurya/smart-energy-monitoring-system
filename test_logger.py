from sensors.sensor_simulator import SensorSimulator
from energy.energy_calculator import EnergyCalculator
from data.energy_logger import EnergyLogger

sensor = SensorSimulator()
calculator = EnergyCalculator()
logger = EnergyLogger()

voltage = sensor.get_voltage()
current = sensor.get_current()

power = calculator.calculate_power(voltage, current)
energy = calculator.calculate_energy(power, time_hours=1)

logger.log(voltage, current, power, energy)

print("Data logged successfully!")
