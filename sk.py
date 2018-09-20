import pandas as pd  ##call pandas library

import matplotlib.pyplot as plt
df=pd.read_csv('df.csv')  ##Load the data set
# print(df.head(30))   ###Have a glipse on the upper part of data set
# print(df.tail(30))     ###Have a glimpse on the lower part of data set

x=df['REGIS_DATE'].unique()  ##count the number of unique days
print(len(x)) ##count the number of days

y=df['REGIS_TIME'].unique()
print(len(y)) #count the number unique of hours

print(len(df['REGIS_TIME']))  ##count the number of people who visited the hospital

print(len(df['REGIS_TIME'])-len(y)) ##the number of hours that had multiple entries

list1=df.groupby(['REGIS_DATE'])['REGIS_TIME'].count()

df1=pd.DataFrame(list1)
print(df1)

print(df1.describe()) ## to get the distribution of the vistiations per day

mean=df.groupby(['REGIS_TIME','REGIS_DATE'])['REGIS_DATE'].sum()
print(mean)

print(df1.hist())
plt.show()
list2=df.groupby(['REGIS_TIME','REGIS_DATE'])['REGIS_TIME'].count()

df2=pd.DataFrame(list2)
print(df2)

data=pd.read_csv('data')

data = data.rename(columns={'REGIS_TIME': 'TIME'})

print(data)


