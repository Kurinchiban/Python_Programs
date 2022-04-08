"""
Encapusulation - Class is an example of encapsulation as it binds all the data members 
                 (instance variables) and methods into a single unit.
"""

class Employee:
    def __init__(self,name,project,salary):
        self.name=name 
        self.project=project 
        self.salary=salary 
    def show(self):
        print("Hi my name is {} and i working on this {} ".format(self.name,self.project))

a=Employee("virat","MPL",50000)
a.show()
