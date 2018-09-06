###A classes stores functions and data(A class start with a capital letter)
class Person:
     def greet(self):
         print("hi")

     def calculate(self):
         print(88*10)

     def add(self,x,y):
         print(x+y)


###Before accessing functions in a class we must create variables
x=Person()
x.greet()
x.calculate()
x.add(7,5)