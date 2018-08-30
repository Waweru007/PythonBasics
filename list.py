#creating a list
scores=[50,23,34,56,76,23,46,21,76,90,30,46,17,89,35,23,24,25,25,29,12,13,14,15,17,18,19,22,23,24,26]

##accessing elements in a list
print(scores)

##print the sixth element
print(scores[5])

##print from the second element onwords
print(scores[2:])

##print last two
print(scores[-2:])

##print the first two
print(scores[:2])

##omit the last two
print(scores[:-2])
score2=scores[:-2]
print(score2)

print("**********************")
##print from the third to the eight element with the uper side  of the set non inclusive
print(scores[2:8])

##looping with a list
for mark in scores:
    print(mark)



