#  linear regression model
#  using the LinearRegression class from scikit-learn.

# Imports for ML
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# End of import

# Generate sample data
np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Split the data into training test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train linear regression model
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

# Make predictions on the test set
y_pred = lin_reg.predict(x_test)

# Evalute the model
mse = mean_squared_error(y_test, y_pred)

# Plot the data and the gression line
plt.scatter(x_test, y_test, color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=3)
plt.show()
