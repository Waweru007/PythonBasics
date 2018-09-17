from testdbs import  Kenyan

k = Kenyan.get(kenyan_id=1)

print(k.names)

k.email_adress="kj@yahoo.com"

k.save()

