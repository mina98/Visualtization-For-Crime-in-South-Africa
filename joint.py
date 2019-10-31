import seaborn as sb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
Pop = pd.read_csv("Dataset/ProvincePopulation.csv")
p = Pop.sort_values(by=['Province'])
# print(p)
# print(Pop.head(10))
# #print('list of features:', Pop.columns.values)
# Pop.plot(x="Province", y="Population",kind='box')
# plt.xlabel('Province')
# plt.ylabel('Population')
# Pop.plot(x="Population", y="Area",kind='scatter')
#
# # Pop.plot(x="Province", y="Population")
# plt.xlabel
# plt.show()
#
Crime = pd.read_csv("Dataset/SouthAfricaCrimeStats_v2.csv")
###############################################################

merGe = pd.merge(left=Pop, right=Crime, on=None, left_on='Province', right_on='Province')

M = merGe.sort_values(by='Province')
# print(M)
merGe_Crimes_Province = M.groupby(['Province', 'Population'])['2015-2016'].sum()
s = pd.DataFrame({'Crimes': M.groupby(['Province', 'Population'])['2015-2016'].sum()}).reset_index()
f = pd.DataFrame({'Crimes': M.groupby(['Province', 'Population', 'Area', 'Density'])['2015-2016'].sum()}).reset_index()

sb.jointplot(x=f['Crimes'],y=f['Population'])
plt.show()