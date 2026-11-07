from scipy.stats import describe


class Pet:

     def __init__(self, name, age):

         self.name = name
         self.age = age

     def speak(self):
         pets = [Dog, Cat, Bird]
         for pets in pets :
             print(describe())

     def describe(self):
        if self.age > 10:
            return f"{self.name} age of {self.age} is a senior"

        else:
            return f"his name is {self.name}, {self.age} of age"

class Dog(Pet):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is barking")

    def fetch(self):
        print(f"{self.name} is going to fetch the stick")

class Bird(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def fly(self):
        print(f"{self.name} fly away from us")

    def speak(self):
        print(f"{self.name} is speaking")

class Cat(Pet):
    def purr(self):
        print(f"{self.name} is busy vibrating lowly on its throat")

    def speak(self):
        print(f"{self.name} is speaking ")
