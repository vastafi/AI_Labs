from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from analyzeClearData import data_set_clean

def linear_regression_analysis(data_set_clean):
    x = data_set_clean.drop('medianCompexValue', axis=1)
    y =data_set_clean['medianCompexValue']

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

    # Performance Metrics Bar Chart
    metrics1 = ['Training MSE', 'Test MSE']
    values1 = [train_mse, test_mse]
    metrics2 = ['Training R²', 'Test R²']
    values2 = [train_r2, test_r2]

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    # Mean Squared Error (MSE)
    ax[0].bar(metrics1, values1, color=['blue', 'orange'])
    ax[0].set_title('Mean Squared Error (MSE)')
    ax[0].set_ylim(0, max(values1) + max(values1)*0.1)  # Adjust the y-axis limit for clarity

    # R-squared Score (R²)
    ax[1].bar(metrics2, values2, color=['green', 'red'])
    ax[1].set_title('R-squared Score (R²)')
    ax[1].set_ylim(0, 1)  # The limit for R² should be between 0 and 1

    plt.show()

linear_regression_analysis(data_set_clean)