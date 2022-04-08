# Generator - It is a kind of iterator (generator function)

def simpleGeneratorFun():
    yield 1
    yield 2 
    yield 3 

a=simpleGeneratorFun()
print(a.next())
print(a.next())
print(a.next())

#----------#
#sending value to the generator

def numberGenerator(n):
     number = yield
     while number < n:
         number = yield number 
         number += 1

g = numberGenerator(10)    
next(g)                    
print(g.send(5))

#--------#
# next() to itrate thre generator

def numberGenerator(n):
     number = 0
     while number < n:
         yield number
         number += 1

g = numberGenerator(10)

counter = 0

while counter < 10:
    print(next(g))
    counter += 1
