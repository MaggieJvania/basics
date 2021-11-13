"""
Chapter 9
Object-oriented programming - modeling the real world object and using them in program
Class - model of something; generic state(description) and behavior of object(car, dog, tree, human...)
object - instance of class; one of the sample of model;
instantiation - creating
self - keyword that shows variable and functions belongs to current class (in java "this" keyword)

"""

class Dog():
    """
    this is the model for generic dog.
    """
    # state/property/instance variable: name, color, breed, age
         # state/property: number_of_leg = 4
    def __init__(self, name, color, breed, age):
        """Initialize variables name, color, breed, age."""
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    # behavior: run(), sit(), bark()
    def run(self):
        print(f"{self.name.title()} is running...")

    def sit(self):
        print(f"{self.name.title()} is sitting:)")

    def bark(self):
        print(f"{self.name.title()} says woof woof!!!")

    def description(self):
        print(f"Hi this is {self.name}, I am a beautiful {self.color} colored dog. I am {self.age} years old {self.breed}.")


class Cat():
    def __init__(self):
        # in this case constructor is optional since python creates automatically
        pass # do nothing in python

    def sit(self):
        print("cats dont like to sit so I will lay down.")


