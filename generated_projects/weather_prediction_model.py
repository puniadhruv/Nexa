
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

# Assume you have a dataframe 'df' with temperature and precipitation columns
data = pd.read_csv('weather_data.csv')  # Replace this line with your actual data loading code
X = data[['temperature', 'precipitation']]
y = data['weather']  # The predicted weather, for example, 'Rainy' or 'Sunny' could be encoded as integers

# Prepare the dataset by encoding the categorical column and splitting it into training and testing sets
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('MSE: ', mse)
print('R^2 Score: ', r2)
