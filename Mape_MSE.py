# Creating a Function for MAPE
import numpy as np

def calculate_mape(y_test, pred):
    y_test, pred = np.array(y_test), np.array(pred)
    mape = round(np.mean(np.abs((y_test - pred) / y_test))*100,3)
    return mape

def calculate_mse(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    differences = np.subtract(actual, predicted)
    squared_differences = np.square(differences)
    return round(squared_differences.mean()*100,3)