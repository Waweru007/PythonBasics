#import all the math library in order to use its functions using an asterisk(*)
from math import *
# from math import  sqrt
scores=[50,23,34,56,76,23,46,21,76,90,30,46,17,89,35,23,24,25,25,29,12,13,14,15,17,18,19,22,23,24,26]
radius=19.56
print(sqrt(radius))
root=sqrt(radius)
print(round(root))

##Values inside a function are argumnets or parameters
print(pow(radius, 2))
power=round(pow(radius,2))
print(power)

##You can call a fucntion within a function(nesting)

x="10.5"

#convert string to a number
z=int("6")
##convert to a float
h=float(x)
y=10
print(z*y*h)


marks=["12","13","34", "454", "29"]
marks_int=[]

for mark in marks:
    marks_int.append(int(mark))
print(marks)
print(marks_int)

#sort in assending order
sorted_scores= sorted(scores)
print(sorted_scores)

#sort in dessending order
sorted_discending=sorted(scores, reverse=True)
print(sorted_discending)

#split a string based on spaces  "I #went# to# a #supermarket", print the resulting array
sentence= "I went to the supermarket yesterday"


split_sentence=sentence.split(" ")
print(split_sentence)


#calculates area of equ triangle
legth=16
area=(sqrt(3)/4)*pow(legth,2)
print(area)

#reverse a string  john nhoj
name="john"
reverse_name=name[::-1]
print(reverse_name)




