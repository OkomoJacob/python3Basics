class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name} and I am talking...")

john = Person("John Smith")
john.talk()

bob = Person("Bob Collimore")
bob.talk()