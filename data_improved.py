import requests
import time
import csv

# simulator URL
url = "http://localhost:9797/poll"

# csv file path
file_path = "data_improved.csv"

# function to extract values
def extract_value(data, key):

    parts = data.split()

    for i in range(len(parts)):

        if parts[i] == key:
            return parts[i + 1]

    return None


# open csv file
with open(file_path, "w", newline="") as f:

    writer = csv.writer(f)

    # csv columns
    writer.writerow([
        "otemp",
        "humidity",
        "wind",
        "thermostat",
        "tempA"
    ])

    print("Starting data collection...")

    # collect data
    for _ in range(200):

        response = requests.get(url)

        data = response.text

        # extract values
        otemp = extract_value(data, "otemp")
        humidity = extract_value(data, "rhm")
        wind = extract_value(data, "wdsp")
        thermostat = extract_value(data, "tsp/A")
        tempA = extract_value(data, "temp/A")

        # verify values exist
        if (
            otemp is not None and
            humidity is not None and
            wind is not None and
            thermostat is not None and
            tempA is not None
        ):

            # convert Kelvin to Celsius
            otemp_c = float(otemp) - 273.15

            # save row
            writer.writerow([
                otemp_c,
                float(humidity),
                float(wind),
                float(thermostat),
                float(tempA)
            ])

            # display values
            print(
                "Outside Temp:", round(otemp_c, 2),
                "| Humidity:", humidity,
                "| Wind:", wind,
                "| Thermostat:", thermostat,
                "| Room Temp:", tempA
            )

        else:
            print("Some values missing")

        # wait before next request
        time.sleep(0.2)

print()
print("Data collection finished")
print("CSV saved as:", file_path)