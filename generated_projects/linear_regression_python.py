 ```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample dataset with 100 data points and 2 features (x and y)
data = np.random.rand(100, 2)

# Add a constant column of 1s for the intercept term
X = np.column_stack((np.ones(100), data))
y = data[:, 1] + np.random.normal(scale=0.5, size=100)

# Split the dataset into training and testing sets (70% for training, 30% for testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Linear Regression model and fit it to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)
```