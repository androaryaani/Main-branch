from sklearn.linear_model import LinearRegression
import numpy as np

# Sample dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 6, 9, 12, 15])  # y = 3x

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict for x = 6
pred = model.predict([[6]])
print("Prediction for input 6:", pred[0])
