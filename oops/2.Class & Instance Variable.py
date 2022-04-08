# Class variable , Instance variable 

class Employee:
    # Class variable
    workinghours=10
    def __init__(self,name,salary,degree):
        #Instance variable
        self.name=name
        self.salary=salary
        self.degree=degree 
    workinghours=7
    # If the instance variable(workinghours) is not present then it will take from class variable
    def print_details(self):
        print ("name is {},salary is{}, my degree is{} and his working hour is {}".format(self.name,self.salary,self.degree,self.workinghours))
    
rubak=Employee("rubak",100000,"Mechanical") 
rubak.print_details()
print(rubak.workinghours)
print(Employee.workinghours)