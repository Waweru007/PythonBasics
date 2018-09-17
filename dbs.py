from peewee import * ###peewee is the object relational mapper.

db=MySQLDatabase(host="localhost",user="root",password="",database="school")

class Student(Model):
    # student_id=PrimaryKeyField()
    student_id=IntegerField()
    name=CharField()
    maths=IntegerField()
    english=IntegerField()
    chemistry=IntegerField()
    date_done=DateField()
    class Meta:
        database=db
        db_table="results"


# Student.create(email_adress='holt@kk.com',dob='2010-12-19',course='Maths',gender='Female',names='John Holt',country='Sudan')

# x=Student.get(id=5)
#
# print(x.course, x.names)
#
#
# x.names='Silvester Juma'
students =Student.select()
#
# for s in students:
#     print(s.id, s.names)

# x=Student.get(id=5)
# x.delete_instance()

import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame(list(students.dicts()))

print(df.head())
# # df.info()
print(df.count())
#
# print(df.tail())
#
x=df['maths']
y=df['english']
# plt.plot(y)
# plt.hist(y)
# plt.show()
df.boxplot()
df.corr(method='pearson')
h=sum(x)/len(x)
print(h)
print(df.mean())
# print(df.mode())
print(df.describe())
print(df['maths'].describe())
