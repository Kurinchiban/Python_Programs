"""Actual arguments:
            *position
            *keword
            *default 
            *arbitrary positional arguments
            *arbitrary keyword arguments
"""
#position
 
def add(a,b):
    c=a+b 
    return c 

a=add(1,8)
print(a) 

#keword 

def biodata(name,age):
    print(name)
    print(age)

a=biodata(name="kurinchi",age=22) 

#default

def biodata1(name,age=18):
    print(name)
    print(age) 

biodata1("kurinchiban")

#arbitrary positional arguments [*-args (store in tuple)]

def add1(a,*b):
    for i in b: 
        a+=i 
    print(b) # tuple
    print(a)

add1(5,6,3,7,8)

#arbitrary keyword arguments  [*-kwargs (store in dictionary)]

def fn(**a):
    for i in a.items():
        print (i)
    print(a)  #dictionary
fn(numbers=5,colors="blue",fruits="apple")