#Crearing the class and object with attributes
 
class Dog:
    class_attribute="Mammel"
    # Constructor
    def __init__(self,name,breed):
        self.name=name 
        self.breed=breed 

    #Creating the Method inside the class 
    def tell_name(self):
        print("My Name is {}".format(self.name))
        print("My Breed is {}".format(self.breed))
    
#object Tommy (Instance of the class)

Tommy=Dog("Tommy","labrador")
print(Tommy.name) 
print(Tommy.breed)
Tommy.tell_name()
#Calling the class atributes
print("Tommy is also a {}".format(Tommy.__class__.class_attribute))