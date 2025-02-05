import numpy as np
from sklearn import linear_model
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures

# Polynomial Regressions with top three features
def polynomial_regression(x_train, y_train, cols):
    x_train = x_train[cols]
    poly_features = PolynomialFeatures(degree=2)

    # transforms the existing features to higher degree features.
    x_train_poly = poly_features.fit_transform(x_train)

    # fit the transformed features to Linear Regression
    poly_model = linear_model.LinearRegression()
    poly_model.fit(x_train_poly, y_train)

    return poly_model


# Polynomial Regression with all features
def polynomial_regression_all(x_train, x_test, y_train, y_test):
    poly_features = PolynomialFeatures(degree=2)

    # transforms the existing features to higher degree features.
    x_train_poly = poly_features.fit_transform(x_train)

    # fit the transformed features to Linear Regression
    poly_model = linear_model.LinearRegression()
    poly_model.fit(x_train_poly, y_train)

    # predicting on train data-set
    prediction_train = poly_model.predict(x_train_poly)
    error_train = metrics.mean_squared_error(y_train, prediction_train)
    print('Mean Square Error of Polynomial Regression with 7 features on train set: ', error_train)

    # predicting on test data-set
    prediction_test = poly_model.predict(poly_features.fit_transform(x_test))

    error_test = metrics.mean_squared_error(y_test, prediction_test)
    print('Mean Square Error of Polynomial Regression with 7 features on test set: ', error_test)

    return error_train, error_test


# Polynomial Regressions with top three features
def polynomial_regression_top_three(x_train, x_test, y_train, y_test):
    x_train = x_train[:, [1, 4, 6]]
    x_test = x_test[:, [1, 4, 6]]
    poly_features = PolynomialFeatures(degree=2)

    # transforms the existing features to higher degree features.
    x_train_poly = poly_features.fit_transform(x_train)

    # fit the transformed features to Linear Regression
    poly_model = linear_model.LinearRegression()
    poly_model.fit(x_train_poly, y_train)

    # predicting on train data-set
    prediction_train = poly_model.predict(x_train_poly)
    error_train = metrics.mean_squared_error(y_train, prediction_train)
    print('Mean Square Error of Polynomial Regression with top 3 features on train set: ', error_train)

    # predicting on test data-set
    prediction_test = poly_model.predict(poly_features.fit_transform(x_test))
    error_test = metrics.mean_squared_error(y_test, prediction_test)
    print('Mean Square Error of Polynomial Regression with top 3 features on test set: ', error_test)

    return error_train, error_test


# Polynomial Regression with all features
def polynomial_regression_all(x_train, x_test, y_train, y_test):
    poly_features = PolynomialFeatures(degree=2)

    # transforms the existing features to higher degree features.
    x_train_poly = poly_features.fit_transform(x_train)

    # fit the transformed features to Linear Regression
    poly_model = linear_model.LinearRegression()
    poly_model.fit(x_train_poly, y_train)

    # predicting on train data-set
    prediction_train = poly_model.predict(x_train_poly)
    error_train = metrics.mean_squared_error(y_train, prediction_train)
    print('Mean Square Error of Polynomial Regression with 7 features on train set: ', error_train)

    # predicting on test data-set
    prediction_test = poly_model.predict(poly_features.fit_transform(x_test))

    error_test = metrics.mean_squared_error(y_test, prediction_test)
    print('Mean Square Error of Polynomial Regression with 7 features on test set: ', error_test)

    return error_train, error_test


# Polynomial Regressions with top three features
def polynomial_regression_top_three(x_train, x_test, y_train, y_test):
    x_train = x_train[:, [1, 4, 6]]
    x_test = x_test[:, [1, 4, 6]]
    poly_features = PolynomialFeatures(degree=2)

    # transforms the existing features to higher degree features.
    x_train_poly = poly_features.fit_transform(x_train)

    # fit the transformed features to Linear Regression
    poly_model = linear_model.LinearRegression()
    poly_model.fit(x_train_poly, y_train)

    # predicting on train data-set
    prediction_train = poly_model.predict(x_train_poly)
    error_train = metrics.mean_squared_error(y_train, prediction_train)
    print('Mean Square Error of Polynomial Regression with top 3 features on train set: ', error_train)

    # predicting on test data-set
    prediction_test = poly_model.predict(poly_features.fit_transform(x_test))
    error_test = metrics.mean_squared_error(y_test, prediction_test)
    print('Mean Square Error of Polynomial Regression with top 3 features on test set: ', error_test)

    return error_train, error_test
