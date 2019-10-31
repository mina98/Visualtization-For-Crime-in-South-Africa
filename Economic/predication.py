import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

# creating file handler for
# our example.csv file in
# read mode
file_handler = open("../Dataset/gold.csv", "r")

# creating a Pandas DataFrame
# using read_csv function that
# reads from a csv file.
data = pd.read_csv(file_handler, sep=",")

# closing the file handler
file_handler.close()

# traversing through Gender
# column of dataFrame and
# writing values where
# condition matches.

data.Date[data.Date.str.contains('2005')] = '1'
print(data['Date'])
Gold = pd.read_csv('gold.csv')
print(Gold[Gold['Date'].str.contains('2005')]['USD (AM)'])
feature_name=['1','USD (AM)']
targetname=['USD (AM)']
x=[1,Gold[feature_name]]
y=Gold[Gold['Date'].str.contains('2005')]['USD (AM)']
print(x.head())
print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123)
linear_regression_model=LinearRegression()
linear_regression_model.fit(x_train,y_train)
y_pred_test=linear_regression_model.predict(x_test)
error=mean_squared_error(y_pred=y_pred_test)
print(error)