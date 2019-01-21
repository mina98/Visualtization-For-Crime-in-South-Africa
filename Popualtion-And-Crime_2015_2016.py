import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
Pop = pd.read_csv("ProvincePopulation.csv")
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
Crime = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
###############################################################
argv=sys.argv
print(argv[1])
merGe = pd.merge(left=Pop, right=Crime, on=None, left_on='Province', right_on='Province')

M = merGe.sort_values(by='Province')
# print(M)
merGe_Crimes_Province = M.groupby(['Province', 'Population'])['2015-2016'].sum()
s = pd.DataFrame({'Crimes': M.groupby(['Province', 'Population'])['2015-2016'].sum()}).reset_index()
f = pd.DataFrame({'Crimes': M.groupby(['Province', 'Population', 'Area', 'Density'])['2015-2016'].sum()}).reset_index()

if(argv[1]=='1'):
    merGe_Crimes_Province.plot(kind='bar', rot=10, color='#2f00ff')
    plt.title('Crime per province and Population')
    plt.xlabel('province and Population')
    plt.ylabel('Crime ')

    plt.show()

# f=M[].sum()
elif(argv[1] is '2'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(f['Crimes'], f['Population'], f['Density'])
    plt.legend()
    ax.grid(True)

    ax.set_xlabel('Crimes')
    ax.set_ylabel('Population')
    ax.set_zlabel('Density')
# print(Repo_Gold_Crimes_Years.corr())

    plt.show()
elif(argv[1]=='3'):
    s.plot(x='Population', y='Crimes', kind='scatter')
    plt.title('Crime per Population')
    plt.show()

# sns.heatmap(s.corr(), annot=True, fmt=".2f")
# plt.show()
elif(argv[1]=='4'):
    sns.set(style="ticks")
    sns.pairplot(f, diag_kind="kde")
    plt.show()
elif(argv[1]=='5'):
    sns.heatmap(f.corr(), annot=True, fmt=".2f")
    plt.show()
elif(argv[1]=='6'):

    sns.heatmap(f.cov(), annot=True)

    plt.show()
    print(merGe.cov())

