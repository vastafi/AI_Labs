import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, ElasticNet, Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV

# Define the file path
file_path = "/Users/astafivalentina/PycharmProjects/AILabs/4.LinearRegression/apartmentComplexData.csv"

# Initialize an empty list to hold each row's data
data = []

# Open the file and read line by line
with open(file_path, 'r') as file:
    for line in file:
        # Strip leading/trailing whitespace and double quotes, then split by comma
        split_line = line.strip().strip('"').split(',')
        # Convert each item to float and append to the data list
        data.append([float(item) for item in split_line])

# Define the column names based on the provided details
column_names = ['longitude', 'latitude', 'complexAge', 'totalRooms', 'totalBedrooms',
                'complexInhabitants', 'apartmentsNr', 'otherFeature', 'medianCompexValue']

# Create a DataFrame from the data list
data_set = pd.DataFrame(data, columns=column_names)

interested_columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']
data_set_interest = data_set[interested_columns]

# Define the features and the target variable
x = data_set_interest.drop('medianCompexValue', axis=1)  # Features
y = data_set_interest['medianCompexValue']  # Target variable

# Split the dataset into training (80%) and testing (20%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(x_train, y_train)

# Predict on the training set and the test set
y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)

# Calculate the model's performance metrics
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Training Mean Squared Error (MSE): {train_mse}")
print(f"Test Mean Squared Error (MSE): {test_mse}")
print(f"Training R-squared Score: {train_r2}")
print(f"Test R-squared Score: {test_r2}")

# Actual vs Predicted
plt.scatter(y_test, y_test_pred)
plt.xlabel('Actual values')
plt.ylabel('Predicted values')
plt.title('Actual vs Predicted values')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.show()

# Residuals Plot
residuals = y_test - y_test_pred
plt.scatter(y_test_pred, residuals)
plt.xlabel('Predicted values')
plt.ylabel('Residuals')
plt.hlines(y=0, xmin=y_test_pred.min(), xmax=y_test_pred.max(), colors='red')
plt.title('Residuals Plot')
plt.show()

# Performance Metrics Bar Chart
metrics1 = ['Training MSE', 'Test MSE']
values1 = [train_mse, test_mse]
metrics2 = ['Training R²', 'Test R²']
values2 = [train_r2, test_r2]

plt.bar(metrics1, values2, color=['blue', 'orange'])
plt.title('Model Performance Metrics')
plt.show()

plt.bar(metrics2, values2, color=[ 'green', 'red'])
plt.title('Model Performance Metrics')
plt.show()