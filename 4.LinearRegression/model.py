from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from analyzeClearData import data_set_clean

x = data_set_clean.drop('medianCompexValue', axis=1)
y = data_set_clean['medianCompexValue']

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