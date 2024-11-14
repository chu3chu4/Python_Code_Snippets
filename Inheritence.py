class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("a mammal is created")

    def run(self):
        print ("all mammals can run")

class Dog(Mammal):
    def __init__ (self, name, age):
        super().__init__(name, age)
        print("a dag is created")
        print(f"the name of the dog is {self.name}, and it is {self.age} years old")

    def bark(self, message):
        print(f"Woof! woof! this is {self.name} barking and I can say {message}")

    def run(self):
        super().run()
        print("message from Dog class's first run method")

    #the run method would overwrite the run method above, even though the number of parameters are different
    """
    def run(self, distance):
        print("message from Dog class's 2nd run method")
        print(f"I can run {distance} meters")
    """

dog1 = Dog("sara", 4)
dog1.bark("nihao")
dog1.run()