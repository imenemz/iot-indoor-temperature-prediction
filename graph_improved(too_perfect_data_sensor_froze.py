import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load data
data = pd.read_csv("data_improved.csv")

# remove empty values
data = data.dropna()

# inputs
X = data[[
    "otemp",
    "thermostat",
    "door1",
    "door2",
    "roller1",
    "roller2",
    "motion"
]]

# output
y = data["tempA"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("Total rows:", len(data))
print("Test rows:", len(X_test))

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# predictions
y_pred = model.predict(X_test)

# graph
plt.figure(figsize=(10,5))

plt.plot(
    range(len(y_test)),
    y_test.values,
    label="Real temperature"
)

plt.plot(
    range(len(y_pred)),
    y_pred,
    label="Predicted temperature"
)

plt.xlabel("Test samples")
plt.ylabel("Temperature (°C)")
plt.title("Real vs Predicted Temperature")

plt.legend()
plt.grid()

plt.show()

print("visualisation done")