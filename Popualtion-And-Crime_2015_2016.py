import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Pop = pd.read_csv("ProvincePopulation.csv")
p=Pop.sort_values(by=['Province'])
print(p)
#print(Pop.head(10))
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
Crime = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
###############################################################
merGe=pd.merge(left=Pop, right=Crime,on = None, left_on = 'Province', right_on = 'Province')
# print(merGe.head(10))
M=merGe.sort_values(by='Province')
# print(M)
merGe_Crimes_Province = M.groupby(['Province','Population'])['2015-2016'].sum()
merGe_Crimes_Province.plot(kind='bar',rot=10)
plt.show()
plt.title('Crime per province and Population')
###############################################################
s=pd.DataFrame({'Crimes' : M.groupby(['Province','Population'])['2015-2016'].sum()}).reset_index()
# f=M[].sum()
print(s)
s.plot(x='Population',y='Crimes')

plt.xlabel('Crime')
plt.ylabel('Population')
plt.title('Crime per Population')
plt.show()
s.plot(x='Population',y='Crimes',kind='scatter')
plt.title('Crime per Population')
plt.show()
s.plot(x='Population',y='Crimes',kind='box',color='black',rot=10)
plt.show()
# print(s.corr())
sns.heatmap(s.corr(), annot=True, fmt=".2f")
plt.show()
sns.heatmap(merGe.corr(), annot=True, fmt=".2f")
plt.show()