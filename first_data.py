import requests
import time
import csv
import os

url = "http://localhost:9797/poll"

file_path = r"C:\Users\ASUS\OneDrive - Université Côte d'Azur\imene_uni\L3\S6\ia_obj\first_data.csv"


def extract_value(data, key):
    parts = data.split()

    for i in range(len(parts)):
        if parts[i] == key:
            return float(parts[i + 1])

    return None


# crée un fichier avec les data de temp
with open(file_path, "w", newline="") as f:

    writer = csv.writer(f)
    writer.writerow(["otemp", "tempA"])

    for _ in range(500):

        response = requests.get(url)
        data = response.text

        otemp = extract_value(data, "otemp")
        tempA = extract_value(data, "temp/A")

        if otemp is not None and tempA is not None:

            otemp_C = otemp - 273.15
            writer.writerow([otemp_C, tempA])

            # we only take the outside temp and inside temp
            print("Outside temp:", otemp_C, "°C | Room A temp:", tempA, "°C")

        else:
            print("error: value not found")

        time.sleep(0.1)

print(os.getcwd())
print("data collection is done")
print("the file was saved in:")
print(file_path)
