#OOPS: Object-Oriented Programming
#OOPS is a programming paradigm that organizes code around objects, which are instances of classes.
#Classes: blueprints for creating objects. They define attributes (data) and methods (functions) that operate on the data.
#Objects: instances of classes. They can have their own unique data and behavior.
#OOP models real-world objects in code. Examples: employee, bank account, machine, customer.
#Why OOP Matters?
#1. Encapsulation: OOP allows you to bundle data and methods that operate on that data within a single unit (class). This helps protect the internal state of an object and prevents unintended interference.
#2. Inheritance: OOP allows you to create new classes that inherit attributes and methods from existing classes.
#3. Polymorphism: OOP allows objects of different types to be treated as instances of the same type through a common interface. This promotes flexibility and code reuse.
#4. Abstraction: OOP allows you to hide complex implementation details and expose only the necessary features of an object. This simplifies the interface and makes it easier to use.
#Large systems become easier to manage.Used in enterprise software, SAP, banking applications, backend systems.
'''class Student:

    def greet(self): # This defines METHOD behavior.
        print("Hello Student")
student1 = Student()#This creates OBJECT.
student1.greet()'''

class Car:
    def start_engine(self):
        print("start_engine()")
Actual_BMW_car = Car()
Actual_BMW_car.start_engine()