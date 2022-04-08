# Using the class function as a alternative constructor

class Employee:
    # class variable
    workinghours=10
    def __init__(self,name,salary,degree):
        #Instance variable
        self.name=name
        self.salary=salary
        self.degree=degree 
    def print_details(self):
        print ("name is {},salary is{}, my degree is {} and his working hour is {}".format(self.name,self.salary,self.degree,self.workinghours))
    #Class method to change the class variable while calling the function
    @classmethod 
    def changeworkinghours(cls,newworkinghour):
        cls.workinghours=newworkinghour # Class variable
    @classmethod
    def spliter(cls,string):
        spliting=string.split("-")
        return cls(spliting[0],spliting[1],spliting[2])

kumar=Employee.spliter("Kumar-10000-CS")
kumar.print_details()