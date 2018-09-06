class Person: ##Constractor fanction is the init function which is used to set up data in a class
    def __init__(self, names, weight, height):
        self.names= names
        self.weight=weight
        self.height=height
    def great(self):
        print("Hello " +self.names)

    def calc_Bmi(self):
        result=self.weight/(self.height**2)
        print(self.names,"Has a BMI of", result)
#Account-Class
##withdrwaw-Fxn to reduce balance
#deposit_fxn to increase the balance
#Check balance



##We create the objects below(Objects are variables created from a class)
p1=Person("Mike",50,1.85)
p2=Person("Peter", 80,1.65)
p3=Person("Wesh", 86, 1.45)

p1.great()
p2.great()
p3.great()
p1.calc_Bmi()
p2.calc_Bmi()
p3.calc_Bmi()