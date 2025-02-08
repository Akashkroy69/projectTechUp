# Regression (Simplified Overview)

# Regression is a statistical method used to find relationships between variables and predict one variable based on another.
# Why Use Regression?

# It helps answer questions like:

#     How does house size affect price?
#     How does studying time affect test scores?

# Types of Regression (Basic)

#     Linear Regression:
#         Predicts a continuous output.
#         Finds a straight line (y = mx + b) that best fits the data.

#     Example: Predicting house price based on size.


# smaple data
import numpy as np
from sklearn.linear_model import LinearRegression
xHouseSize  = np.array([[1000], [1500], [2000], [2500], [3000]])  # House size in square feet
yHousePrice = np.array([[500000], [700000], [800000], [900000], [1000000]])  # House price in thousands of dollars

model = LinearRegression()
model.fit(xHouseSize, yHousePrice)

# enter size of house to predict price
size = int(input("Enter the size of the house: "))

predictedPrie = model.predict([[size]])
print("the predicted price of the house is: ", predictedPrie[0])


# Steps in Regression

#     Collect Data: Gather features (X) and target (y).
#     Train Model: Fit the model to the data.
#     Make Predictions: Use the model to predict new data.
#     Evaluate: Check the model’s accuracy.






#     Logistic Regression:
#         Predicts a categorical output.
#         Finds the probability of a binary outcome.

#     Example: Predicting if a student will pass or fail based on study time.

#     Polynomial Regression:
#         Predicts a continuous output.
#         Fits a curve to the data.

#     Example: Predicting stock prices based on historical data.

#     Ridge Regression:
#         Reduces the complexity of the model.
#         Adds a penalty to the size of the coefficients.

#     Example: Predicting house price based on size, age, and location.

#     Lasso Regression:
#         Reduces the complexity of the model.
#         Adds a penalty to the absolute size of the coefficients.

#     Example: Predicting house price based on size, age, and location.

