# lambda <args>: <statement> 
# map(fun, iter)
#sorted(iterable, key, reverse)

a=lambda x,y : print(x+y) 
a(5,7)

list_2=[454,34,5,67,87,55]
list_3=list(map(lambda x : x%2==0,(list_2)))
print(list_2)
print(list_3)

ids = ["id1", "id2", "id30", "id3", "id20", "id10"]
b=sorted(ids,key=lambda x: int(x[2:]))
print(b)

print((lambda x, y: x * y)(2, 3))

print((lambda x:(x % 2 and 'odd' or 'even'))(4))

# using the lambda in function 

def myfun(n):
    return lambda a:a*3 
mytripler=myfun(3)
print(mytripler(11))




