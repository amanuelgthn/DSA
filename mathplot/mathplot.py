#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Simulated dataset (based on the description provided)
data = {
    "CPI": [234.16, 144, 133.85, 111.07, 163.52, 149.75, 123.78, 101.87, 202.92, 151.36,
            110.5, 143.82, 281.66, 133.61, 103.62, 116.76, 167.4, 261.73, 112.85, 195.76,
            113.53, 135.87, 124.74, 110.05, 117.24, 118.4, 124.35, 232.75, 114.24, 117.7,
            117.56, 167.18, 121.46, 223.13, 151.18, 109.82, 106.58],
    "Minimum_wage": [0.57, 1.57, 0.18, 1.6, 0.73, 0.29, 2.25, 4.46, 1.66, 0.95,
                     0.68, 1.55, 0.84, 0.05, 0.71, 9.51, 1.53, 0.71, 9.99, 0.65,
                     4.33, 0.83, 0.88, 11.16, 7.25, 3.85, 1.05, 3.35, 11.49, 0.6,
                     0.78, 0.32, 0.93, 0.17, 0.48, 2.92, 0.34],
    "Unemployment_rate": [0.0443, 0.1269, 0.0424, 0.0902, 0.0201, 0.1819, 0.0398, 0.1724, 0.0873, 0.117,
                          0.1225, 0.0481, 0.0888, 0.144, 0.0434, 0.0556, 0.1208, 0.0689, 0.0304, 0.0601,
                          0.0267, 0.0063, 0.0947, 0.0843, 0.147, 0.0593, 0.0643, 0.0979, 0.0407, 0.0189,
                          0.0836, 0.0234, 0.0332, 0.0281, 0.0469, 0.0693, 0.0626],
    "Fertility": [4.26, 1.49, 5.92, 2.42, 2.05, 2.87, 1.71, 1.35, 1.97, 3.02,
                  2.27, 2.43, 1.3, 2.06, 4.21, 1.5, 1.73, 5.52, 1.56, 2.9,
                  2.89, 2.67, 4.43, 1.88, 1.73, 2.32, 4.51, 2.26, 1.71, 5.75,
                  3.88, 1.98, 2.0, 4.32, 2.31, 1.47, 5.19]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Independent and dependent variables
X = df[["CPI", "Minimum_wage", "Unemployment_rate"]]
y = df["Fertility"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Coefficients and Intercept
coefficients = model.coef_
intercept = model.intercept_

# Plotting actual vs predicted
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='Perfect Prediction')
plt.title("Regression Model: Predicted vs Actual Fertility")
plt.xlabel("Actual Fertility")
plt.ylabel("Predicted Fertility")
plt.legend()
plt.grid()
plt.show()

# Output results
print("Mean Squared Error (MSE):", mse)
print("Coefficients:", coefficients)
print("Intercept:", intercept)
