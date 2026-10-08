from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd

# load data
df = pd.read_csv("first_data.csv")

# remove empty values if they exist
df = df.dropna()

X = df[["otemp"]]   # input: outside temperature
y = df["tempA"]     # output: room A temperature

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# test model
y_pred = model.predict(X_test)

# calculate errors
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("MSE:", mse)
print("MAE:", mae)

# show model equation
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

# example prediction
test = pd.DataFrame([[15]], columns=["otemp"])
prediction = model.predict(test)

print("Prediction for 15°C outside:", prediction[0])