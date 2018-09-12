#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyspark as spark
from pyspark.sql import SparkSession

spark=SparkSession    .builder    .appName("Python SQL Example")    .config("spark.some.config.option","same-value")    .getOrCreate()
    


# In[6]:


from pyspark.sql import SQLContext


# In[7]:


###df=spark.read.csv('C:/Users/Wesh/Desktop/creditcard.csv')
df=spark.read    .options(header=True, inferSchema=True)    .csv('MOCK_DATA.csv')
    
df1=spark.read    .options(header=True, inferSchema=True)    .csv('MOCK_DATA.csv')


##df2=spark.read.csv('E:/Python/ECMO_Imputed.csv')


# In[16]:


df.head(10)


# In[17]:


df1.head(2)


# In[10]:


df.printSchema()


# In[33]:


df.count


# In[36]:


# df.describe().show()


# In[6]:


# df.dropna().count()  ###drop null values and count the number of droped numbers 


# In[14]:


# df2=df.fillna(-1).show(5) ###fill the missing values with -1 and shows the first five values


# In[19]:


df.select("names").show()


# In[28]:


df.filter(df['salary']<210).show()


# In[42]:


df.groupBy("salary").count().show()


# In[46]:


# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")


# In[49]:


All= spark.sql("SELECT * FROM people LIMIT 10")
All.show()


# In[55]:


age1996=spark.sql("SELECT * FROM people WHERE dob LIKE '%2018%'")
age1996.show()


# In[ ]:




