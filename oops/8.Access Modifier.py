"""
public       This modifier is accesed by everyone outside the class
private      This modifier is not accesed by outside of the class 
             and the inheritance used inside the class
proteceted   This modifier not acessed by outside the class 
             but can accessed by inside of the inheritance of the class
"""
class Employee:
    var=10              #  public
    __varprivate=100    #  private
    _varprotected=1000  #  protected
    def __init__(self,name,salary,degree):
        self.name=name
        self.salary=salary
        self.degree=degree 
    
    def print_private(self):
        print ("I an private {}".format(self.__varprivate))
    def print_protected(self):
        print ("I an protected {}".format(self._varprotected))
    
class programmer(Employee):
    def __init__(self,name,salary,degree,program):
        self.name=name
        self.salary=salary
        self.degree=degree 
        self.program=program

    # Cannot access the private function or variable inside the inheritance of the class
    def program_details_private(self):
        print ("I an private {}".format(self.__varprivate))

    def program_details_protected(self):
        print("I an protected {}".format(self._varprotected))

rubak=Employee("rubak",100000,"Mechanical")
rubak.print_private()
rubak.print_protected()
ragul=programmer("Ragul",18000,"Ec","python")
#ragul.program_details_private()
ragul.program_details_protected()
print(Employee._varprotected)