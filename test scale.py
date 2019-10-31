import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import boxcox
from sklearn import preprocessing
import numpy as nm
# from sklearn.preproces5sing import scale
df=pd.read_csv("Dataset/SouthAfricaCrimeStats_v2.csv")
# dx=sb.distplot(df['2005-2006'],rug=True,hist=False,color='#505050')
# dx.axvline(x=df['2005-2006'].mean(),color='#505050',linestyle='-')
# plt.xlim(0,3500)
# plt.show()
col=df['2005-2006']
new=[]
new2=[]
for i in range(len(col)):
    if col[i]>0:
        new.append(col[i])
    else:
        new2.append(col[i])
# summ=XX.sum()
# list=XX.tolist()
# new=[]

# for i in range(len(list)):
#     new.append(list[i]*1000/summ)
# print("new list : " + str(new))
# dx=sb.distplot(new,rug=True,hist=False,color='r')
# m=sum(new)/len(new)
# dx.axvline(x=m,color='#505050',linestyle='-')
# plt.xlim(-1,3)
# plt.show()
pt = preprocessing.PowerTransformer(method='box-cox', standardize=False)
new=nm.reshape(new,(-1,1))
new_trans=pt.fit_transform(new)
newww=new_trans.tolist()
print(newww)

listt=[]
for i in range(len(newww)):
    listt.append(newww[i][0])
kolcol=new2 + listt

kolcol=pd.DataFrame(kolcol)
print(kolcol)
m=kolcol.mean()
mm=m[0]
print(mm)
dx=sb.distplot(kolcol,rug=True,hist=False,color='#505050')
dx.axvline(x=mm,color='#505050',linestyle='-')
plt.show()
#for_trans=df['2005-2006'].values
#print(for_trans)

