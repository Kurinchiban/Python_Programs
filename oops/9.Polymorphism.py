#Polymporphism 


# len() being used for a string
print(len("geeks"))
# len() being used for a list
print(len([10, 20, 30]))

#Polymorphism with Inheritance:[Method Overriding]

class Father:
  def age(self):
    print("My age is 40")
  def colour(self):
    print("My colour is White")
class son(Father):
  def age(self):
    print("My age is 18")
  def colour(self):
    print("My colour is Black")

a=Father()
b=son()
#same Function but different operation
a.age()
b.age()
a.colour()
b.colour() 
