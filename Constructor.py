# Constructor in Python
# A constructor is a special method in a class that is automatically called when an object of the class is created. It is used to initialize the attributes of the object.
# In Python, the constructor method is defined using the __init__() method. The __init__() method takes at least one parameter, self, which refers to the instance of the class being created. You can also include additional parameters to initialize other attributes of the object.
# The __init__() method is called automatically when you create an object of the class, and it allows you to set up the initial state of the object by assigning values to its attributes.
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

student1 = Student("Joseph")
student1.greet()