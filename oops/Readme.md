         Python OOPs Concepts

    • The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.
      
      Class:[A class is a code template for creating objects]
    • A class is a collection of objects. A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods.
    • Classes are created by keyword class.
    • Attributes are the variables that belong to a class.
    • Attributes are always public and can be accessed using the dot (.) operator. 
      Eg.: Myclass.Myattribute
      
      Class variable:
    • Class variable shared by all object instances of a class 
    • They are not defined inside any methods of a class.
    • Class variable can be changed by using the class method (@classmethod)
      
      Instance variable:
    • The variables given below the constructor are called instance variable
    • For every object, a separate copy of the instance variable
      
      Static Method:
    • Calling the simple function inside the class and it definatly placed inside the class
      
      Object : [An object is simply a collection of data (variables) and methods that act on those data]
    • The object is an entity that has a state and behavior associated with it
    • State:It is represented by the attributes of an object. It also reflects the properties of an object.Ex: The identity can be considered as the name of the dog.
      Behavior:It is represented by the methods of an object. It also reflects the response of an object to other objects.State or Attributes can be considered as the breed, age, or color of the dog.
      Identity:It gives a unique name to an object and enables one object to interact with other objects.The behavior can be considered as to whether the dog is eating or sleeping.
      
      Self:[Refering Object]
    • Self is always pointing to Current Object.
    • self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
      
      __init__:[It is costructor the code will run when we call the class]
    • constructor
    • It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
      
      Inheritance:[Inherit the code from the super class to sub class]
    • inheritance is the capability of one class to inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class
    • It provides the reusability of a code. 
    • It allows us to add more features to a class without modifying it.
      
      Polymorphism:[Same Function but different data type or output as a result]
    • The word polymorphism means having many forms. 
    •  polymorphism means the same function name being used for different types.
      Encapsulation:[Wraping up of a data under a single unit][Data Hiding]
    • This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. 
      
      Object Method:
    • public : This modifier is accesed by everyone outside the class
    • private : This modifier is not accesed by outside of the class and the inheritance used inside the class 
    • protected : This modifier not acessed by outside the class but can accessed by inside of the inheritance of the class
      
      Abstraction :[Hiding the unecessary data for the user]
    • Abstraction is defined as a process of handling complexity by hiding unnecessary information from the user.
      
      Overriding: [Searching the variable in class (subclass) ]
    • Initialy search (from subclass) a variable inside the instance class then it will search for the main class instance then it will go for the subclass-class variable and the it will go and search in the mainclass- class varable (if the constructor presernt in the subclass the above method will not work)
