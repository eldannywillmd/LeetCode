import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Create dummy data
data = pd.DataFrame({
    'passengers': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    'duration': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'street_closed': [True, False, True, False, True, False, True, False, True, False],
    'day_of_week': [1, 2, 3, 4, 5, 6, 7, 1, 2, 3],
    'month': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'year': [2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020, 2020],
    'net_sales': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
})

# Define features and target
features = ['passengers', 'duration', 'street_closed', 'day_of_week', 'month', 'year']
target = 'net_sales'

X = data[features]
y = data[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
assert mae < 1000, "Mean Absolute Error is too high!"

def update_model(model, new_data):
    # Append the new data to the original data
    global X, y
    X = pd.concat([X, new_data[features]])
    y = pd.concat([y, new_data[target]])

    # Retrain the model
    model.fit(X, y)

    return model

# Create some new data
new_data = pd.DataFrame({
    'passengers': [1500, 2500, 3500],
    'duration': [11, 12, 13],
    'street_closed': [False, True, False],
    'day_of_week': [4, 5, 6],
    'month': [11, 12, 1],
    'year': [2021, 2021, 2022],
    'net_sales': [11000, 12000, 13000]
})

# Update the model
model = update_model(model, new_data)

# Evaluate the updated model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
assert mae < 1000, "Mean Absolute Error is too high!"
