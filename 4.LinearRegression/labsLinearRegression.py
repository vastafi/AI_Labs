import pandas as pd
import seaborn as sns
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

# Select only the columns of interest
interested_columns = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr', 'medianCompexValue']
data_set_interest = data_set[interested_columns]

# Generate descriptive statistics
descriptive_stats = data_set_interest.describe()


# Check for missing values in the dataset
print(data_set_interest.isnull().sum())

# Pandas describe() is used to view some basic statistical details of a data frame
print(data_set_interest.describe())

# Pandas info() function is used to get a concise summary of the dataframe.
print(data_set_interest.info())

# Histograms for each feature
data_set_interest.hist(bins=50, figsize=(20, 15))
plt.show()

# Visualize data distribution for each column


# Task 2

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

# Task 3 Assuming these are the feature names used during model training
feature_names = ['complexAge', 'totalRooms', 'totalBedrooms', 'complexInhabitants', 'apartmentsNr']

# New house features for prediction
new_house_features = {
    'complexAge': [12],
    'totalRooms': [3000],
    'totalBedrooms': [500],
    'complexInhabitants': [800],
    'apartmentsNr': [400]
}

# Convert the features into a pandas DataFrame
new_house_df = pd.DataFrame(new_house_features, columns=feature_names)

# Predict using the model
predicted_price = model.predict(new_house_df)

print(f"Predicted median complex value for the new house: {predicted_price[0]}")

# Plot the distribution of 'medianCompexValue'
plt.figure(figsize=(10, 6))
sns.histplot(data_set_interest['medianCompexValue'], kde=True, color="blue", label='Distribution of Prices')

# Mark the predicted price on the plot
plt.axvline(x=predicted_price[0], color='red', linestyle='--', linewidth=2, label='Predicted Price')

plt.xlabel('Median complex value')
plt.ylabel('Frequency')
plt.title('Distribution of median complex value with prediction')
plt.legend()

plt.show()

# Set up a figure for subplotting
plt.figure(figsize=(18, 12))  # Adjust the figure size as needed

# Scatter plot: Age vs. Price
plt.subplot(2, 3, 1)
plt.scatter(data_set_interest['complexAge'], data_set_interest['medianCompexValue'], color="blue")
plt.title("Dependency between Age and Price")
plt.xlabel("Complex Age")
plt.ylabel("Price in U/M")

# Scatter plot: Total Rooms vs. Price
plt.subplot(2, 3, 2)
plt.scatter(data_set_interest['totalRooms'], data_set_interest['medianCompexValue'], color="red")
plt.title("Dependency between Number of Rooms and Price")
plt.xlabel("Number of Rooms")
plt.ylabel("Price in U/M")

# Scatter plot: Total Bedrooms vs. Price
plt.subplot(2, 3, 3)
plt.scatter(data_set_interest['totalBedrooms'], data_set_interest['medianCompexValue'], color="green")
plt.title("Dependency between Number of Bathrooms and Price")
plt.xlabel("Number of Bathrooms")
plt.ylabel("Price in U/M")

# Scatter plot: Complex Inhabitants vs. Price
plt.subplot(2, 3, 4)
plt.scatter(data_set_interest['complexInhabitants'], data_set_interest['medianCompexValue'], color="yellow")
plt.title("Dependency between Number of Inhabitants and Price")
plt.xlabel("Inhabitants in Complex")
plt.ylabel("Price in U/M")

# Scatter plot: Apartments Number vs. Price
plt.subplot(2, 3, 5)
plt.scatter(data_set_interest['apartmentsNr'], data_set_interest['medianCompexValue'], color="orange")
plt.title("Dependency between Number of Apartments and Price")
plt.xlabel("Number of Apartments in Complex")
plt.ylabel("Price in U/M")

# Distribution plot for 'medianCompexValue'
plt.subplot(2, 3, 6)
sns.histplot(data_set_interest['medianCompexValue'], color='r', kde=True)  # Added kde=True for kernel density estimate
plt.title("Distribution of Price")
plt.xlabel("Price in U/M")

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Compute the correlation matrix
corr_matrix = data_set_interest.corr()

# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, square=True)
plt.title('Correlation Matrix with Heatmap')
plt.show()


# Task 4

# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(x_train, y_train)
linear_train_pred = linear_reg.predict(x_train)
linear_test_pred = linear_reg.predict(x_test)
linear_train_mse = mean_squared_error(y_train, linear_train_pred)
linear_test_mse = mean_squared_error(y_test, linear_test_pred)
linear_train_r2 = r2_score(y_train, linear_train_pred)
linear_test_r2 = r2_score(y_test, linear_test_pred)

print("Linear Regression:")
print(f"Training MSE: {linear_train_mse}")
print(f"Test MSE: {linear_test_mse}")
print(f"Training R²: {linear_train_r2}")
print(f"Test R²: {linear_test_r2}")
print("\n")

# Ridge Regression model
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(x_train, y_train)
ridge_train_pred = ridge_reg.predict(x_train)
ridge_test_pred = ridge_reg.predict(x_test)
ridge_train_mse = mean_squared_error(y_train, ridge_train_pred)
ridge_test_mse = mean_squared_error(y_test, ridge_test_pred)
ridge_train_r2 = r2_score(y_train, ridge_train_pred)
ridge_test_r2 = r2_score(y_test, ridge_test_pred)

print("Ridge Regression:")
print(f"Training MSE: {ridge_train_mse}")
print(f"Test MSE: {ridge_test_mse}")
print(f"Training R²: {ridge_train_r2}")
print(f"Test R²: {ridge_test_r2}")
print("\n")

# Lasso Regression model
lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(x_train, y_train)
lasso_train_pred = lasso_reg.predict(x_train)
lasso_test_pred = lasso_reg.predict(x_test)
lasso_train_mse = mean_squared_error(y_train, lasso_train_pred)
lasso_test_mse = mean_squared_error(y_test, lasso_test_pred)
lasso_train_r2 = r2_score(y_train, lasso_train_pred)
lasso_test_r2 = r2_score(y_test, lasso_test_pred)

print("Lasso Regression:")
print(f"Training MSE: {lasso_train_mse}")
print(f"Test MSE: {lasso_test_mse}")
print(f"Training R²: {lasso_train_r2}")
print(f"Test R²: {lasso_test_r2}")
print("\n")

# Elastic Net model
elastic_net = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_net.fit(x_train, y_train)
elastic_train_pred = elastic_net.predict(x_train)
elastic_test_pred = elastic_net.predict(x_test)
elastic_train_mse = mean_squared_error(y_train, elastic_train_pred)
elastic_test_mse = mean_squared_error(y_test, elastic_test_pred)
elastic_train_r2 = r2_score(y_train, elastic_train_pred)
elastic_test_r2 = r2_score(y_test, elastic_test_pred)

print("Elastic Net Regression:")
print(f"Training MSE: {elastic_train_mse}")
print(f"Test MSE: {elastic_test_mse}")
print(f"Training R²: {elastic_train_r2}")
print(f"Test R²: {elastic_test_r2}")

# Define a set of alpha values for Ridge regression
parameters = {'alpha': [0.01, 0.1, 1.0, 10.0, 100.0]}

ridge = Ridge()
ridge_regressor = GridSearchCV(ridge, parameters, scoring='neg_mean_squared_error', cv=5)
ridge_regressor.fit(x_train, y_train)

# Best parameters and MSE
print("\nBest alpha:", ridge_regressor.best_params_)
print("Best MSE:", -ridge_regressor.best_score_)

# Extracting MSE and R² scores
train_mse_scores = [linear_train_mse, ridge_train_mse, lasso_train_mse, elastic_train_mse]
test_mse_scores = [linear_test_mse, ridge_test_mse, lasso_test_mse, elastic_test_mse]
train_r2_scores = [linear_train_r2, ridge_train_r2, lasso_train_r2, elastic_train_r2]
test_r2_scores = [linear_test_r2, ridge_test_r2, lasso_test_r2, elastic_test_r2]


# Models names
models = ['Linear', 'Ridge', 'Lasso', 'Elastic Net']

# Plotting MSE scores
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
bar_width = 0.35
index = range(len(models))
plt.bar(index, train_mse_scores, bar_width, color='b', alpha=0.5, label='Train MSE')
plt.bar([i + bar_width for i in index], test_mse_scores, bar_width, color='r', alpha=0.5, label='Test MSE')
plt.xlabel('Models')
plt.ylabel('MSE Scores')
plt.title('Comparison of MSE Scores')
plt.xticks([i + bar_width / 2 for i in index], models)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Plotting R² scores
plt.subplot(1, 2, 2)
plt.bar(index, train_r2_scores, bar_width, color='b', alpha=0.5, label='Train R²')
plt.bar([i + bar_width for i in index], test_r2_scores, bar_width, color='r', alpha=0.5, label='Test R²')
plt.xlabel('Models')
plt.ylabel('R² Scores')
plt.title('Comparison of R² Scores')
plt.xticks([i + bar_width / 2 for i in index], models)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()