from main import Dog, Bird, Cat

dog = Dog(name="Rocky", age=11, breed="Cane corso")
bird = Bird(name="John", age=5, breed="Crow")
cat = Cat(name="Jake", age=9)

print(f"\nI have a dog, {dog.describe()}")
print(f"{dog.name} is a {dog.breed} type of dog")
dog.speak()
dog.fetch()

print(f"\nI have a bird, {bird.describe()}")
print(f"{bird.name} is a {bird.breed} type of a bird ")
bird.speak()
bird.fly()

print(f"\nI have a cat {cat.describe()}")
cat.speak()
cat.purr()

