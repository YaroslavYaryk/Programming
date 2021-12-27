from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def grow(self):
        pass

class Child(Parent):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow(self):
        print(f"my name is {self.name} and my age is {self.age}")



child = Child("Yarosav", 18)
child.grow()

