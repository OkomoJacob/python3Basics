class Mammal:
    def walk(self):
        print("Walking...")

class Dog(Mammal):
    def bark(self):
        print("Barking...")


class Cat(Mammal):
    def meow(self):
        print("Cat is Meowing...")


dog = Dog()
dog.walk()
dog.bark()
cat = Cat()
cat.meow()
