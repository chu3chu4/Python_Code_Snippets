class Dog:
    def __init__(self, color, age):
        self.colour = color
        self.ages = age
        print(f"Hey, I am a dog, and I am in {self.colour} color, and I am {self.ages} years old")


dog1 = Dog("gold", 4)
dog2 = Dog("brown", 8)
dog3 = Dog("silve", 10)