# Exp 01: Simple Linear Regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # Study hours
y = np.array([35, 40, 50, 55, 65, 70])            # Exam scores

model = LinearRegression().fit(X, y)
pred = model.predict(X)
print("Slope:", model.coef_[0], "Intercept:", model.intercept_)
print("Prediction at 7 hours:", model.predict([[7]])[0])
print("MSE:", mean_squared_error(y, pred), "R2:", r2_score(y, pred))

plt.scatter(X, y)
plt.plot(X, pred)
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.show()
