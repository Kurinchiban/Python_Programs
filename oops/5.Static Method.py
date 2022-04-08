# Static method

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
    @classmethod
    def spliter(cls,string):
        spliting=string.split("-")
        return cls(spliting[0],spliting[1],spliting[2])
    # Creating the simple function inside the class
    @staticmethod 
    def print_things(string):
        print("This is {}".format(string))

kumar=Employee.spliter("Kumar-10000-CS")
kumar.print_details()
kumar.print_things("KUMAR")