# Overriding

class A:
    c1var="I am a class varable inside class A"
    def __init__(self):
        self.var1="I am inside the constroctor of class A"
        self.c1var="I'm in the constroctor of class A"
class B(A):
    c1var="I am a class var inside the B"
    
a=A()
b=B()
print(b.c1var)
print(a.c1var)

#-------------------#

# If the constuctor presen in the class b then it will not go to the super class

class A:
    c1var="I am a class varable inside class A"
    def __init__(self):
        self.var1="I am inside the constroctor of class A"
        self.c1var="I'm in the constroctor of class A"
class B(A):
    c1var="I am a class var inside the B"
    def __init__(self):
        self.var1="I am inside the constroctor of class B"
        #self.c1var="I'm in the constroctor of class B"
a=A()
b=B()
print(b.c1var)

#----ERROR----#

# while using the super.__init__ we can use the constroctor of class A

class A:
    c1var="I am a class varable inside class A"
    def __init__(self):
        self.var1="I am inside the constroctor of class A"
        self.c1var="I'm in the constroctor of class A"
        self.special="Special"
class B(A):
    #c1var="I am a class var inside the B"
    def __init__(self):
        super().__init__()
        self.var1="I am inside the constroctor of class B"
        self.c1var="I'm in the constroctor of class B"
a=A()
b=B()
print(b.special)
