class Point: #A class is a blueprint to create our objects 
    def move(self):
        print("I'm moving...")

    def draw(self):
        print("I'm drawing...")

point1 = Point() #Point() is the object # An object is an instance of a class
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)

point2 = Point()
