import time

from sensors.sensor_simulator import SensorSimulator
from energy.energy_calculator import EnergyCalculator
from data.energy_logger import EnergyLogger
from analytics.anomaly_detection import AnomalyDetector
from analytics.bill_prediction import BillPredictor
from cloud.thingspeak_client import ThingSpeakClient
from config.settings import TIME_INTERVAL, THINGSPEAK_API_KEY


def main():
    # TEMPORARY: check if API key is loaded
    print("API key loaded:", THINGSPEAK_API_KEY)

    # Initialize all modules
    sensor = SensorSimulator()
    calculator = EnergyCalculator()
    logger = EnergyLogger()
    detector = AnomalyDetector()
    bill_predictor = BillPredictor()
    cloud = ThingSpeakClient()

    total_energy = 0  # in kWh

    print("\nSmart Energy Monitoring System Started...")
    print("Press CTRL + C to stop\n")

    try:
        while True:
            voltage = sensor.get_voltage()
            current = sensor.get_current()

            power = calculator.calculate_power(voltage, current)
            energy = calculator.calculate_energy(power, TIME_INTERVAL / 3600)

            total_energy += energy

            logger.log(voltage, current, power, energy)

            if detector.is_high_consumption(power):
                print("⚠️ ALERT: High energy consumption detected!")

            cloud.upload(power, energy)

            estimated_bill = bill_predictor.calculate_bill(total_energy)

            print(
                f"Voltage: {voltage} V | "
                f"Current: {current} A | "
                f"Power: {power} W | "
                f"Total Energy: {round(total_energy, 4)} kWh | "
                f"Estimated Bill: ₹{estimated_bill}"
            )

            time.sleep(TIME_INTERVAL)

    except KeyboardInterrupt:
        print("\nSystem stopped by user.")
        print(f"Final Energy Used: {round(total_energy, 4)} kWh")
        print(f"Final Bill Amount: ₹{bill_predictor.calculate_bill(total_energy)}")


if __name__ == "__main__":
    main()
