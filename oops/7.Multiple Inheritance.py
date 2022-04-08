#Multiple Inheritance

class Employee:
   
    def __init__(self,name,job,salary):
        self.name=name
        self.job=job
        self.salary=salary

    def print_employee(self):
        print("It is {},my job is {} and my salary is {} ".format(self.name,self.job,self.salary))
        
class Business(Employee):
    def __init__(self,name,job,salary,business):
        self.name=name
        self.job=job
        self.salary=salary
        self.business=business

    def print_Bemployee(self):
        print("I do {} as my business".format(self.business))

class Sports:
    def __init__(self,game):
        self.game=game 
    def pprint(self):
        print("I play {} game".format(self.game))

class SmartEmployee(Employee,Sports):
    pass 

""" 
    The SmartEmployee will access 
    if constructor present inside that class
    if not it will go for next class (Employee)
    if constructor present inside that class 
    it will run 
    otherwise it will go to the next class Sports
"""
p1=SmartEmployee("rubak","programmer",10000)
p1.print_employee()
#p1.print_Bemployee()
#p2=SmartEmployee("cricket")
#p2.pprint()


