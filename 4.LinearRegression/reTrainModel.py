from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from analyzeClearData import data_set_clean
def linear_regression_analysis(data_set_clean):
    x = data_set_clean.drop('medianCompexValue', axis=1)
    y =data_set_clean['medianCompexValue']

    # Split the dataset into training (80%) and testing (20%) sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()

    model.fit(x_train, y_train)

    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    print("\n Linear Regression:")
    print(f"Training Mean Squared Error (MSE): {train_mse}")
    print(f"Test Mean Squared Error (MSE): {test_mse}")
    print(f"Training R-squared Score: {train_r2}")
    print(f"Test R-squared Score: {test_r2}")

linear_regression_analysis(data_set_clean)
def ridge_regression_analysis(data_set_clean, alpha=1.0):
    x = data_set_clean.drop('medianCompexValue', axis=1)
    y = data_set_clean['medianCompexValue']

    # Split the dataset into training (80%) and testing (20%) sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = Ridge(alpha=alpha)

    model.fit(x_train, y_train)

    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    print(f"\n Ridge Regression with alpha={alpha}:")
    print(f"Training Mean Squared Error (MSE): {train_mse}")
    print(f"Test Mean Squared Error (MSE): {test_mse}")
    print(f"Training R-squared Score: {train_r2}")
    print(f"Test R-squared Score: {test_r2}")

ridge_regression_analysis(data_set_clean, alpha=0.1)

def lasso_regression_analysis(data_set_clean, alpha=1.0):
    x = data_set_clean.drop('medianCompexValue', axis=1)
    y = data_set_clean['medianCompexValue']

    # Split the dataset into training (80%) and testing (20%) sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = Lasso(alpha=alpha)

    model.fit(x_train, y_train)

    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    print(f"\n Lasso Regression with alpha={alpha}:")
    print(f"Training Mean Squared Error (MSE): {train_mse}")
    print(f"Test Mean Squared Error (MSE): {test_mse}")
    print(f"Training R-squared Score: {train_r2}")
    print(f"Test R-squared Score: {test_r2}")

lasso_regression_analysis(data_set_clean, alpha=0.1)

def elastic_net_regression_analysis(data_set_clean, alpha=1.0, l1_ratio=0.5):
    x = data_set_clean.drop('medianCompexValue', axis=1)
    y = data_set_clean['medianCompexValue']

    # Split the dataset into training (80%) and testing (20%) sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)

    model.fit(x_train, y_train)

    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    print(f"\n Elastic Net Regression with alpha={alpha} and l1_ratio={l1_ratio}:")
    print(f"Training Mean Squared Error (MSE): {train_mse}")
    print(f"Test Mean Squared Error (MSE): {test_mse}")
    print(f"Training R-squared Score: {train_r2}")
    print(f"Test R-squared Score: {test_r2}")

elastic_net_regression_analysis(data_set_clean, alpha=0.1, l1_ratio=0.5)
