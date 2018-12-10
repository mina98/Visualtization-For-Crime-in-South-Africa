import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
import seaborn as sn

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
Repo=pd.read_csv('reporate.csv')
Crime=pd.read_csv('../SouthAfricaCrimeStats_v2.csv')
Gold=pd.read_csv('gold.csv')
list_Of_Years = ['2005-2006', '2006-2007', '2007-2008', '2008-2009',
                 '2009-2010', '2010-2011', '2011-2012',
                 '2012-2013', '2013-2014', '2014-2015', '2015-2016']
Crimes=[]
Crimes.append( Crime['2005-2006'].sum())
Crimes.append( Crime['2006-2007'].sum())
Crimes.append( Crime['2007-2008'].sum())
Crimes.append( Crime['2008-2009'].sum())
Crimes.append( Crime['2009-2010'].sum())
Crimes.append( Crime['2010-2011'].sum())

Crimes.append( Crime['2011-2012'].sum())
Crimes.append( Crime['2012-2013'].sum())
Crimes.append( Crime['2013-2014'].sum())
Crimes.append( Crime['2014-2015'].sum())
Crimes.append( Crime['2015-2016'].sum())


print(Crimes)
Repos=[]
Repos.append(Repo[Repo['Date'].str.contains('2005')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2005')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2006')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2006')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2007')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2007')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2008')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2008')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2009')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2009')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2010')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2010')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2011')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2011')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2012')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2012')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2013')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2013')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2014')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2014')]['TheValue'].count())
Repos.append(Repo[Repo['Date'].str.contains('2015')]['TheValue'].sum()/Repo[Repo['Date'].str.contains('2015')]['TheValue'].count())
print(Repos)
Golds=[]
Golds.append(Gold[Gold['Date'].str.contains('2005')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2005')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2006')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2006')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2007')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2007')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2008')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2008')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2009')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2009')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2010')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2010')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2011')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2011')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2012')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2012')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2013')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2013')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2014')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2014')]['USD (AM)'].count())
Golds.append(Gold[Gold['Date'].str.contains('2015')]['USD (AM)'].sum()/Gold[Gold['Date'].str.contains('2015')]['USD (AM)'].count())
print(Golds)

Repo_Gold_Crimes_Years=pd.DataFrame({'Reporate':Repos,'Crimes':Crimes,'Golds':Golds,'Year':list_Of_Years})
print(Repo_Gold_Crimes_Years)
# plt.scatter(x=Repos,y=Crimes)
# plt.xlabel('RepoRate')
# plt.ylabel('Criems')
# plt.title('Crimes Per RepoRate')
# plt.show()
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(Repo_Gold_Crimes_Years['Reporate'],Repo_Gold_Crimes_Years['Crimes'],Repo_Gold_Crimes_Years['Golds'])

ax.set_xlabel('Reporate')
ax.set_ylabel('Crimes')
ax.set_zlabel('Golds')
print(Repo_Gold_Crimes_Years.corr())

plt.show()
sn.set(style="ticks")
sn.pairplot(Repo_Gold_Crimes_Years.corr())

plt.show()

sn.pairplot(Repo_Gold_Crimes_Years, diag_kind="kde")

plt.show()
sn.pairplot(Repo_Gold_Crimes_Years,  kind="reg")
plt.show()

sn.heatmap(Repo_Gold_Crimes_Years.corr(), annot=True, fmt=".2f")

plt.show()