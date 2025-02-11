# 2. Polynomial Regression

# If the relationship between data points is curved, Linear Regression won’t work well.
# For example:

#     The relationship between hours studied and test scores may be curved (more studying helps up to a point).

# Polynomial Regression can fit a curved line to the data.

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# Sample data (Time of day vs temperature)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])  # Time of day (hours)
y = np.array([15, 18, 20, 22, 21, 19, 16, 14])  # Temperature (in degrees)

poly = PolynomialFeatures(degree=2)  # Create a PolynomialFeatures object of degree 2
X_poly = poly.fit_transform(X)  # Transform the input data to include polynomial terms

print(X_poly)
model = LinearRegression()
model.fit(X_poly, y)

# Predict the temperature at 4.5 hours
time = 4.5
time_poly = poly.transform([[time]])  # Transform the input data to include polynomial terms
predicted_temp = model.predict(time_poly)
print("The predicted temperature at", time, "hours is:", predicted_temp[0])

# Plot the data
import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue',label="actual data")
plt.plot(X, model.predict(X_poly), color='red',label="predicted data")
plt.xlabel("Time of Day (hours)")  # X-axis label
plt.ylabel("Temperature (°C)")  # Y-axis label
plt.title("Temperature Prediction using Polynomial Regression")  # Plot title
plt.legend()
plt.show()  # Show the plot