from peewee import * ###peewee is the object relational mapper.

db=MySQLDatabase(host="localhost",user="root",password="",database="school")

class Kenyan(Model):
    kenyan_id=PrimaryKeyField()
    email_adress=CharField()
    names=CharField()
    gender=CharField()
    class Meta:
        database=db
        db_table="kenyans"

# Kenyan.create_table()
# Kenyan.create(email_adress="kk@yahoo.com",names="KJ Kenya",gender="M")