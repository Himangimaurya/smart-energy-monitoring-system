import pandas as pd
import matplotlib.pyplot as plt


def show_dashboard():
    """
    Display energy monitoring dashboard
    """

    # Load logged data
    df = pd.read_csv("data/energy_log.csv")

    if df.empty:
        print("No data available to display.")
        return

    # Convert timestamp to readable format if needed
    time_data = df["timestamp"]

    # -------- Power vs Time --------
    plt.figure()
    plt.plot(time_data, df["power"])
    plt.xlabel("Time")
    plt.ylabel("Power (Watts)")
    plt.title("Power Consumption Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # -------- Energy vs Time --------
    plt.figure()
    plt.plot(time_data, df["energy"])
    plt.xlabel("Time")
    plt.ylabel("Energy (kWh)")
    plt.title("Energy Consumption Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    show_dashboard()
