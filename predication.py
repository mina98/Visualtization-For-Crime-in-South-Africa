import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
from collections import OrderedDict
# creating file handler for
# our example.csv file in
# read mode
Gold = pd.read_csv('SouthAfricaCrimeStats_v2.csv')
list_Of_Years = [ '2014-2015', '2015-2016']

targetname=['USD (AM)']
x=Gold[list_Of_Years]
y=Gold['2015-2016']
print(x.head())
print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123)
linear_regression_model=LinearRegression()
linear_regression_model.fit(x_train,y_train)
y_pred_test=linear_regression_model.predict(x_test)
error=mean_squared_error(y_pred=y_pred_test,y_true=y_test)
print(error)
fig,ax=plt.subplots()
ax.scatter(y_test,y_pred_test)
ax.plot(y_test,y_test,color='red')
ax.set_xlabel('Testing')
ax.set_ylabel('perdict')
plt.show()
new_data=OrderedDict([
    ('2014-2015',.4),
('2015-2016',.7)
])
new_data=pd.Series(new_data).values.reshape(-1,1)
linear_regression_model.predict(new_data)