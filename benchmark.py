
import asyncio
import os
from datetime import datetime

from tapo import ApiClient, EnergyDataInterval
import csv
import matplotlib.pyplot as plt


async def main():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    ip_address = os.getenv("IP_ADDRESS")
    
    client = ApiClient(tapo_username, tapo_password)
    device = await client.p110(ip_address)

    print("Turning device on...")
    await device.on()

    device_info = await device.get_device_info()
    print(f"Device info: {device_info.to_dict()}")

    device_usage = await device.get_device_usage()
    print(f"Device usage: {device_usage.to_dict()}")

    current_power = await device.get_current_power()
    print(f"Current power: {current_power.to_dict()}")

    energy_usage = await device.get_energy_usage()
    print(f"Energy usage: {energy_usage.to_dict()}")

    # Create empty lists to store data
    timestamps = []
    power_values = []
    filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    # Create a single figure and axes object
    timer = 0
    plt.show(block=False)
    plt.figure(figsize=(10, 6))
    plt.xlabel("Timestamp")
    plt.ylabel("Power (W)")
    plt.title("Continuous Power Readings")
    while timer < 2 * 60:
        await asyncio.sleep(1)
        current_power = await device.get_current_power()
        print(f"Current power: {current_power.to_dict()}")

        timestamps.append(datetime.now())
        power_values.append(current_power.to_dict()["current_power"])
        # Write current time and power_value to CSV
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Power (W)"])
            for timestamp, power_value in zip(timestamps, power_values):
                writer.writerow([timestamp, power_value])
        timer += 1
        plt.clf()
        plt.plot(timestamps, power_values)
        plt.draw()
        plt.pause(0.1)

    plt.show(block=True)


def get_quarter_start_month(today: datetime) -> int:
    return 3 * ((today.month - 1) // 3) + 1


if __name__ == "__main__":
    asyncio.run(main())
