import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset (replace with your own or load from a CSV)
data = {
    'square_feet': [1500, 1600, 1700, 1800, 2000, 2200],
    'bedrooms':     [3, 3, 4, 4, 5, 5],
    'bathrooms':    [2, 2, 2, 3, 3, 4],
    'price':        [300000, 320000, 340000, 360000, 400000, 450000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['square_feet', 'bedrooms', 'bathrooms']]
y = df['price']

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)

print("Predicted Prices:", y_pred)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))

# Optional: View model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
