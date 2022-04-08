# Class method

class Employee:
    # Class variable
    workinghours=10
    def __init__(self,name,salary,degree):
        #Instance variable
        self.name=name
        self.salary=salary
        self.degree=degree 
    def print_details(self):
        print ("name is {},salary is{}, my degree is{} and his working hour is {}".format(self.name,self.salary,self.degree,self.workinghours))
    #Class method to change the class variable using the function
    @classmethod 
    def changeworkinghours(cls,newworkinghour):
        cls.workinghours=newworkinghour # Class variable

rubak=Employee("rubak",100000,"Mechanical")
rubak.print_details()
rubak.changeworkinghours(7)
rubak.print_details()