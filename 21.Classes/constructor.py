# A constructor is a function with the same name as the class and gets called at the time of creating an object
class Point: 
    def __init__(self, x, y): #constructor
        self.x = x
        self.y = y
    def move(self):
        print("I'm moving...")

    def draw(self):
        print("I'm drawing...")


point1 = Point(10, 20) 
point1.x = 12
print(point1.x)
