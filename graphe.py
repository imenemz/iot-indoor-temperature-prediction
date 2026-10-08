import pandas as pd
import matplotlib.pyplot as plt

#load data
df = pd.read_csv("First_data.csv")

#nettoyage des données vides 
df = df.dropna()


plt.figure(figsize=(8,5))

plt.scatter(df["otemp"], df["tempA"])

#lables
plt.xlabel("Outside temperature (C)")
plt.ylabel("Room A temperature (C)")
plt.title("Room A temperature vs Outside temperature")

#plot grid
plt.grid(True)

plt.show()

print("visualisation done")