
f =open("test.txt", "r") #open the file read mode Read Only (‘r’), Read and Write (‘r+’), Write Only (‘w’) Write and Read (‘w+’)
mes=f.read()  #read the message in the file
print(mes)    ##Print the message in the file
f.close()

f = open('test.txt','a')  ##Append Only (‘a’)  Append and Read (‘a+’)
f.write('\n' + 'Wallace')
print(mes)
f.close()



names=["mike","Tosh", "Peter", "Josh", "Jack"]

print(names)

for name in names:
    f=open("test.txt", "a")
    f.write('\n' + name)
    f.close()
