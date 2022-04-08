# Single Inheritance

class Employee:

    workinghours=10

    def __init__(self,name,salary,degree):
        self.name=name
        self.salary=salary
        self.degree=degree 

    def print_details(self):
        print ("name is {},salary is{}, my degree is{} and his working hour is {}".format(self.name,self.salary,self.degree,self.workinghours))
    
    @classmethod
    def spliter(cls,string):
        spliting=string.split("-")
        return cls(spliting[0],spliting[1],spliting[2])
    
class programmer(Employee):
    def __init__(self,name,salary,degree,workinghours,program):
        self.name=name
        self.salary=salary
        self.degree=degree 
        self.workinghour=workinghours
        self.program=program

    def program_details(self):
        print ("name is {},salary is{}, my degree is{} and his working hour is {} at last he know {}".format(self.name,self.salary,self.degree,self.workinghours,self.program))

kumar=Employee.spliter("Kumar-10000-CS")
kumar.print_details()
ragul=programmer("Ragul",18000,"Ec",9,"python")
ragul.program_details()
ragul.print_details()

