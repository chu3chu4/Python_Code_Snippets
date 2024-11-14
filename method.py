class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        print(f"the name of the dog is {self.name}, and it is {self.age} years old")

    def bark(self, message):
        print(f"Woof! woof! this is {self.name} barking and I can say {message}")
        print()

dog1 = Dog("sara", 4)
dog1.bark("nihao")

dog2 = Dog("Nata", 8)