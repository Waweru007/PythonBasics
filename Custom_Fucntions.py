##Make sure that functions are in a file that does not have other items.

def Area(l,w):
    result=l*w
    return  result


def Volume (l,w,h):
    result=l*w*h
    return result

def sayHi(names):
    return "Hi "+names

def sayHiToMany(names):
    for name in names:
        print("Hi "+name)

def area2(r, pi=3.142, rounded=False):
    result=pi*r**2
    if rounded==True:
        result=round(result)
    return  result

def evenCha(names):
    result=len(names)
    if result % 2==0:
        print("Even")
    else:
        print("Odd")

def compareWord(names, sensitive=True):
    if sensitive==False:
        names= names.lower()
    result=int((len(names)/2))
    left=names[:result]
    right=names[result:]
    if left==right:
        print("Similar")
    else:
        print("Not Similar")

def EvenOrKe(x,y):
    for num in range(x,y):
        if num % 2==0:
            print("Even")
        else:
            print("Kenya")















#call the function
# print(Area(89, 10))
# x=Area(7,5)
#
# print(x)
#
# print(Volume(12,11,10))


