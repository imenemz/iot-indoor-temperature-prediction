import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# load data
data = pd.read_csv("data_improved.csv")

# remove empty values
data = data.dropna()

# inputs
X = data[[
    "otemp",
    "thermostat"
]]

# output
y = data["tempA"]

# split train / test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# model
model = LinearRegression()

# training
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# scores
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model trained successfully")
print()

print("MSE:", mse)
print("MAE:", mae)
print("R2 Score:", r2)

print()

print("Coefficients:")
for name, coef in zip(X.columns, model.coef_):
    print(name, ":", coef)

print()

print("Intercept:", model.intercept_)

# test prediction
test = pd.DataFrame([[

    15,
    26

]], columns=[
    "otemp",
    "thermostat"
])

prediction = model.predict(test)

print()
print("Prediction:", prediction[0], "°C")

print()
print("Rows:", len(data))


print("Columns:")
print(data.columns)