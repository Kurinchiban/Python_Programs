# join 
list_1=["hellow","i","am","kurinchi"]
a="-".join(list_1)
print(a)

#map

def square(a):
    return(a*a)

list_2=["3","4","5","33"]

list_2=list(map(int,(list_2)))
print(list_2)

list_2=list(map(square,(list_2)))
print(list_2)

# Filter

def isgreater(a):
    return a>5

list_3=[1,2,3,4,5,6,7,8,9,10]
list_3=list(filter(isgreater,list_3))
print(list_3) 

#reduce

from functools import reduce

list_4=[1,2,3,4,5,6,7,8,9,10]
num=reduce(lambda x,y:x+y,list_4)
print(num)
