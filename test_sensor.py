from sensors.sensor_simulator import SensorSimulator

sensor = SensorSimulator()

for i in range(5):
    voltage = sensor.get_voltage()
    current = sensor.get_current()
    print(f"Voltage: {voltage} V | Current: {current} A")
