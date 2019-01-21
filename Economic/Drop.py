import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
import seaborn as sn
import numpy as np
import sys

argv = sys.argv
# df=pd.read_csv('oil.csv')
# d=df.drop(df.index[0:5454])
# h=d.drop(df.index[8230:])
# # print(h.tail())
#
# gold=pd.read_csv('gold.csv')
# gold=gold.drop(gold.index[0:9353])
# f=gold.drop(gold.index[12135:12708])
#
# print(f.tail())
Repo = pd.read_csv('reporate.csv')
Crime = pd.read_csv('../SouthAfricaCrimeStats_v2.csv')
Gold = pd.read_csv('gold.csv')
list_Of_Years = ['2005-2006', '2006-2007', '2007-2008', '2008-2009',
                 '2009-2010', '2010-2011', '2011-2012',
                 '2012-2013', '2013-2014', '2014-2015', '2015-2016']
Crimes = []

Crimes.append(Crime['2005-2006'].sum())
Crimes.append(Crime['2006-2007'].sum())
Crimes.append(Crime['2007-2008'].sum())
Crimes.append(Crime['2008-2009'].sum())
Crimes.append(Crime['2009-2010'].sum())
Crimes.append(Crime['2010-2011'].sum())

Crimes.append(Crime['2011-2012'].sum())
Crimes.append(Crime['2012-2013'].sum())
Crimes.append(Crime['2013-2014'].sum())
Crimes.append(Crime['2014-2015'].sum())
Crimes.append(Crime['2015-2016'].sum())

# print(Crimes)
Repos = []
Repos.append(Repo[Repo['Date'].str.contains('2005')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2005')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2006')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2006')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2007')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2007')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2008')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2008')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2009')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2009')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2010')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2010')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2011')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2011')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2012')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2012')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2013')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2013')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2014')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2014')][
    'TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2015')]['TheValue'].sum() / Repo[Repo['Date'].str.contains('2015')][
    'TheValue'].count())
# print(Repos)
Golds = []
Golds.append(Gold[Gold['Date'].str.contains('2005')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2005')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2006')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2006')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2007')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2007')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2008')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2008')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2009')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2009')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2010')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2010')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2011')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2011')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2012')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2012')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2013')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2013')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2014')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2014')][
    'USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2015')]['USD (AM)'].sum() / Gold[Gold['Date'].str.contains('2015')][
    'USD (AM)'].count())
# print(Golds)

Repo_Gold_Crimes_Years = pd.DataFrame({'Reporate': Repos, 'Crimes': Crimes,
                                       'Golds': Golds, 'Year': list_Of_Years})
s = ['Reporate', 'Golds']
# print(Repo_Gold_Crimes_Years[s].head())
if (argv[1] is '1'):
    color2 = ['#800080', '#000080', '#800000', '#B22222', '#006400', 'red', 'blue', 'black', 'green', 'yellow',
              'orange']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(11):
        ax.scatter(Repo_Gold_Crimes_Years['Reporate'][i], Repo_Gold_Crimes_Years['Crimes'][i]
                   , Repo_Gold_Crimes_Years['Golds'][i], label=Repo_Gold_Crimes_Years['Year'][i], color=color2[i])

    plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)

    ax.set_xlabel('Reporate')
    ax.set_ylabel('Crimes')
    ax.set_zlabel('Golds')
    # print(Repo_Gold_Crimes_Years.corr())

    plt.show()
    # elif (argv[1] is '2'):
    #     sn.set(style="ticks")
    #     sn.pairplot(Repo_Gold_Crimes_Years.corr())

    plt.show()
elif (argv[1] is '2'):
    sn.pairplot(Repo_Gold_Crimes_Years, diag_kind="kde")

    plt.show()
elif (argv[1] is '3'):
    sn.heatmap(Repo_Gold_Crimes_Years.corr(), annot=True, fmt=".2f", vmax=0.3)

    plt.show()
elif (argv[1] is '4'):
    sn.heatmap(Repo_Gold_Crimes_Years.cov(), annot=True, fmt=".2f")
    plt.show()
elif (argv[1] is '5'):

    sn.pairplot(Repo_Gold_Crimes_Years, kind="reg")
    plt.show()
elif (argv[1] is '6'):
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    from collections import OrderedDict

    # creating file handler for
    # our example.csv file in
    # read mode
    x = Repo_Gold_Crimes_Years[s]
    y = Repo_Gold_Crimes_Years['Crimes']
    print(x.head())
    # print(y.head())

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)
    print(y_test)
    linear_regression_model = LinearRegression()
    f = linear_regression_model.fit(x_train, y_train)
    print(f)
    y_pred_test = linear_regression_model.predict(x_test)
    print(y_pred_test)
    error = mean_squared_error(y_pred=y_pred_test, y_true=y_test)
    print(error)
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred_test)
    ax.plot(y_test, y_test, color='red')
    ax.set_xlabel('Testing')
    ax.set_ylabel('perdict')
    plt.show()
    # new_data = OrderedDict([
    #     ('Reporate', .4),
    #     ('Golds', .7)
    # ])
    # new_data = pd.Series(new_data).values.reshape(-1,1)
    print(linear_regression_model.predict(np.array([[11], [1000]]).reshape(1, 2)))
