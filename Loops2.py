#creating a list
scores=[50,23,34,56,76,23,46,21,76,90,30,46,17,89,35,23,24,25,25,29,12,13,14,15,17,18,19,22,23,24,26]

#sort in assending order
sorted(scores)

#sort in dessending order
#split a string based on spaces  "I #went# to# a #supermarket", print the resulting array
#calculates area of equ triangle
#reverse a string  john nhoj

#Printing odd scores
print(100%13)
for mark in scores:
    if mark % 2==1:
        print(mark, "odd")
print("---------------------------------")
for mark in scores:
    if mark % 2==0:
        print(mark, "Even")

print("----------------------")

for mark in scores:
     if mark >=80:
         print(mark, "A Pass")

     elif mark>=70 and mark <80:
        print(mark, "B Pass")

     elif mark>=60 and mark <70:
        print(mark, "C Pass")

     elif mark>=50 and mark < 60:
        print(mark, "D Repeat")

     elif mark>=40 and mark < 50:
         print(mark, "E Repeat")
     elif mark <40:
         print(mark, "F Suspended")
###Extract A scores only and Store in a New List
print("------------------------------")
A_scores=[]

for mark in scores:
    if mark >=80:
        A_scores.append(mark)

##Print the scores outside the loop
print(A_scores)