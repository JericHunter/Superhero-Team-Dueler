# dog.py
class Dog:
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # Methods are defined as their own named functions inside the class
    def bark(self):
        print("Woof!")

# my-dogs.py
import dog

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()
my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)