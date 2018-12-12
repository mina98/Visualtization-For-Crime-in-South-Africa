# import plotly.plotly as py
import pandas as pd
import seaborn as sn
from matplotlib import gridspec
import matplotlib.pyplot as plt
import shapefile as shp

import numpy as np

# import argparse

Crime = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
sf = shp.Reader("Police_bounds.shp")

# print(Crime.head(10))
# print(Crime.describe())
list_Of_Years = ['2005-2006', '2006-2007', '2007-2008', '2008-2009',
                 '2009-2010', '2010-2011', '2011-2012',
                 '2012-2013', '2013-2014', '2014-2015', '2015-2016']
Crimes_Province = Crime.groupby(['Province'])[list_Of_Years].sum()
print(Crimes_Province)
Crimes_Category = Crime.groupby(['Category'])[list_Of_Years].sum()
List_Of_Catogeries = Crimes_Category.transpose().columns
# print(List_Of_Catogeries)

CRT = Crimes_Category.transpose()
CRT['index'] = CRT.index

# print('#####################################################')
# print(CRT['index'])
# print('#####################################################')
n = 1
fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
for x in range(0,4):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[x]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        # ax.set_xticklabels(CRT['index'], rotation=35)
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])
        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])
        print("mean of "+List_Of_Catogeries[x * n + j]+" is"+str(CRT[List_Of_Catogeries[x]].mean()))
        print("Variance of " + List_Of_Catogeries[x * n + j] + " is" + str(CRT[List_Of_Catogeries[x]].var()))
        # ax[axc[x][0]][axc[x][1]].set_xticks(rotation='vertical')

plt.show()

fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
x=0
for y in range(4,8):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[y]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        # ax.set_xticklabels(CRT['index'], rotation=35)
        # plt.title(List_Of_Catogeries[x * n + j])
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])

        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])
        print("mean of "+List_Of_Catogeries[y * n + j]+" is"+str(CRT[List_Of_Catogeries[y]].mean()))
        print("Variance of " + List_Of_Catogeries[y * n + j] + " is" + str(CRT[List_Of_Catogeries[y]].var()))
    x=x+1
plt.show()

fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
x=0

ticks=['2005','2008','2011','2014']
for y in range(8,12):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[y]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])

        # ax.set_xticklabels(CRT['index'], rotation=35)
        # plt.title(List_Of_Catogeries[x * n + j])
        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])

        print("mean of "+List_Of_Catogeries[y * n + j]+" is"+str(CRT[List_Of_Catogeries[y]].mean()))
        print("Variance of " + List_Of_Catogeries[y * n + j] + " is" + str(CRT[List_Of_Catogeries[y]].var()))
    x=x+1

plt.show()

fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
x=0
for y in range(12,16):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[y]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        # ax.set_xticklabels(CRT['index'], rotation=35)
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])

        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])
        print("mean of "+List_Of_Catogeries[y * n + j]+" is"+str(CRT[List_Of_Catogeries[y]].mean()))
        print("Variance of " + List_Of_Catogeries[y * n + j] + " is" + str(CRT[List_Of_Catogeries[y]].var()))
    x=x+1

plt.show()
fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
x=0
for y in range(16,20):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[y]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        # ax.set_xticklabels(CRT['index'], rotation=35)
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])

        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])
        print("mean of "+List_Of_Catogeries[y * n + j]+" is"+str(CRT[List_Of_Catogeries[y]].mean()))
        print("Variance of " + List_Of_Catogeries[y * n + j] + " is" + str(CRT[List_Of_Catogeries[y]].var()))
    x=x+1

plt.show()

fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
x=0
for y in range(20,24):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[y]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        # ax.set_xticklabels(CRT['index'], rotation=35)
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])

        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])
        print("mean of "+List_Of_Catogeries[y * n + j]+" is"+str(CRT[List_Of_Catogeries[y]].mean()))
        print("Variance of " + List_Of_Catogeries[y * n + j] + " is" + str(CRT[List_Of_Catogeries[y]].var()))
    x=x+1

plt.show()

fg, ax = plt.subplots(nrows=2, ncols=2)
axc =[(0,0),(0,1),(1,0),(1,1)]
x=0
for y in range(24,27):

    for j in range(n):
        # plt.subplot()
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[y]], color='red' , ax=ax[axc[x][0]][axc[x][1]])
        ax[axc[x][0]][axc[x][1]].set_ylabel("Number of Crimes")
        # ax.set_xlabel("Period")
        # ax.set_xticklabels(CRT['index'], rotation=35)
        ax[axc[x][0]][axc[x][1]].set_xticks([0,11])

        ax[axc[x][0]][axc[x][1]].set_title(List_Of_Catogeries[x * n + j])
        print("mean of "+List_Of_Catogeries[y * n + j]+" is"+str(CRT[List_Of_Catogeries[y]].mean()))
        print("Variance of " + List_Of_Catogeries[y * n + j] + " is" + str(CRT[List_Of_Catogeries[y]].var()))
    x=x+1

plt.show()
# print(CRT['index'])
# print(CRT[List_Of_Catogeries[x]])
# plt.show()
# n = 0
# x=2
# fig,axes=plt.subplots(nrows=3,ncols=3,figsize=(25,15))
# # for x in range(len(List_Of_Catogeries)):
# for row in axes:
#     for col in row:
#         # plt.subplot()
#         sn.barplot(CRT['index'], CRT[List_Of_Catogeries[n]], color='red')
#
#     n = n + 1

# print(CRT['index'])
# print(CRT[List_Of_Catogeries[x]])
plt.show()

Crimes_Province.plot(kind='bar', rot=25)
plt.title('Crime per province')
plt.show()

Crimes_Category[list_Of_Years].transpose().plot(kind='box', rot=90)
plt.title('Crime per Category ')
plt.show()

Crimes_Category[list_Of_Years].plot(kind='box', rot=30)
plt.title('Crime per Years')
plt.show()


# sn.heatmap(Crime.corr(), annot=True, fmt=".2f")
# plt.show()

for shape in sf.shapeRecords():
    # print(shape.shape.points)
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    color=['red','blue']
    plt.plot(x,y,alpha=.7,color='#006400')
    # plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)

plt.show()
# emd east
# titles = list(Crime.columns)
# dates = titles[7:17]
# Crime[dates].plot(kind='scatter')
# plt.xticks(rotation=45)
# plt.title('Overall number of crimes commited for each year')
# plt.show()