import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
# import argparse

Crime = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
# print(Crime.head(10))
# print(Crime.describe())
list_Of_Years = ['2005-2006', '2006-2007', '2007-2008', '2008-2009',
                 '2009-2010', '2010-2011', '2011-2012',
                 '2012-2013', '2013-2014', '2014-2015', '2015-2016']
Crimes_Province = Crime.groupby(['Province'])[list_Of_Years].sum()
# print(Crimes_Province)
Crimes_Category = Crime.groupby(['Category'])[list_Of_Years].sum()
List_Of_Catogeries = Crimes_Category.transpose().columns
print(List_Of_Catogeries)

CRT = Crimes_Category.transpose()
CRT['index'] = CRT.index

# print('#####################################################')
# print(CRT['index'])
# print('#####################################################')
n = 1
for x in range(0, len(List_Of_Catogeries)):
    fg, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 2.5))
    for j in range(n):
        sn.barplot(CRT['index'], CRT[List_Of_Catogeries[x]], color='red')
        ax.set_ylabel("Number of Crimes")
        ax.set_xlabel("Period")
        ax.set_xticklabels(CRT['index'], rotation=35)
        plt.title(List_Of_Catogeries[x * n + j])

    # print(CRT['index'])
    print(CRT[List_Of_Catogeries[x]])
Crimes_Province.plot(kind='bar', rot=25)
plt.title('Crime per province')
Crimes_Category[list_Of_Years].transpose().plot(kind='box', rot=90)
plt.title('Crime per Category ')
Crimes_Category[list_Of_Years].plot(kind='box', rot=30)
plt.title('Crime per Years')
Crimes_Category[list_Of_Years].transpose().plot(kind='line', rot=90)
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
plt.title('Crime per Category')
print(Crime.corr())
#Heatmap
plt.show()
