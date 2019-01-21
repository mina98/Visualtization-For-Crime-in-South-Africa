import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as axm
import seaborn as sb
means1=[]
means2=[]
vars=[]
df = pd.read_csv("SouthAfricaCrimeStats_v2.csv")
list_Of_Years = ['2005-2006', '2006-2007', '2007-2008', '2008-2009',
                 '2009-2010', '2010-2011', '2011-2012',
                 '2012-2013', '2013-2014', '2014-2015', '2015-2016']
Crimes_Category = df.groupby(['Category'])[list_Of_Years].sum()
# print(Crimes_Category)
df=Crimes_Category.transpose()

list_Of_CRIMcat=df.columns
#print(list_Of_CRIMcat)
df=pd.DataFrame(df)
#print(df)
#----------------------------------50 sample of size 50-----------------------------------------------------------------------
for x in range(50):
    # Creating a random sample of the population with size 100:
    sample = df.sample(n=10, replace=True)

    # print(sample['2005-2006'])
    sample = pd.DataFrame(sample)  # convert sample to dataframe for drop

    # print()
     # drop col from df
    sample.index = range(10)
    # print(sample)
    #mean1 = ((sample.sum()) / 500).mean()
    mean2 = ((sample.sum()) / 10)
    var=sample.var()
    # print(mean1)
    # print(mean2)
    # print(mean)

    # Adding this mean to the list of means

    #means1.append(mean1)
    means2.append(mean2)
    vars.append(var)
mean_of_Sample_means2 = pd.DataFrame(means2).mean()
var_of_sample_vars=pd.DataFrame(vars).var()
mean_of_DATA2 = df.mean()
var_of_DATA2=df.var()
print("means of samples :"+str(means2))
print("var of samples   :"+str(vars))
print("mean of sample means :"+ str(mean_of_Sample_means2))
print("var of sample vars :"+str(var_of_sample_vars))
print("mean of all data  : "+str(mean_of_DATA2))
print("var of all data :"+str(var_of_DATA2))
#-----------------------------------samples for ploting-----------------------------------------------------------------
Splot1_1 = df.sample(n=3, replace=True)
#print(Splot1_1['2005-2006'])


# print("sample1/n" + str(Splot1_1))
Splot1_2 = df.sample(n=6 ,replace=True)
# print("sample2/n" + str(Splot1_2))
Splot1_3 = df.sample(n=9, replace=True)
# print("sample3/n"+str(Splot1_3))

for i in range(len(list_Of_CRIMcat)):
    m = mean_of_DATA2[list_Of_CRIMcat[i]]
    #print("sampleOfData"+str(m)+"col"+str(list_Of_CRIMcat[i]))
    M_Splot1_1 = Splot1_1[list_Of_CRIMcat[i]].mean()
    #print("sampleOfs1" + str(M_Splot1_1) + "col" + str(list_Of_CRIMcat[i]))
    M_Splot1_2 = Splot1_2[list_Of_CRIMcat[i]].mean()
    #print("sampleOfs2" + str(M_Splot1_2) + "col" + str(list_Of_CRIMcat[i]))
    M_Splot1_3 = Splot1_3[list_Of_CRIMcat[i]].mean()
    #print("sampleOfs3" + str(M_Splot1_3) + "col" +str(list_Of_CRIMcat[i]))
    #plt.hist(df[list_Of_CRIMcat[i]],bins=30)
    dx =  sb.distplot(df[list_Of_CRIMcat[i]], rug=True, hist=False,color='#000080' ,label="all data")
    dx.axvline(x=m, color='#000080', linestyle='-')

    s1x=sb.distplot(Splot1_1[list_Of_CRIMcat[i]], rug=True, hist=False,color='black' ,label="s1 n=3")
    s1x.axvline(x=M_Splot1_1,color='black',linestyle='-')

    s2x=sb.distplot(Splot1_2[list_Of_CRIMcat[i]], rug=True, hist=False,color='#2ed924',label="s2 n=6")
    s2x.axvline(x=M_Splot1_2,color='#2ed924',linestyle='-')

    s3x = sb.distplot(Splot1_3[list_Of_CRIMcat[i]], rug=True, hist=False,color='r',label="s3 n=9")
    s3x.axvline(x=M_Splot1_3, color='r', linestyle='-')

    plt.legend()
    plt.show()