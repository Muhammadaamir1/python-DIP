class shape:


    #static method
    @staticmethod
    def printype():
        print("print here")
    def draw(self):  # this is call for current class assces  self
        print("draw your world here")
    def area(self):
        print("the area is 10412km")

class rectanlge(shape):
    def __init__(self):
        self.length=0
        self.width=0
    def draw(self):
        print("draw your world here")
    def area(self):
        print("the area is 10412km")

class triangle(shape) :
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
    def draw(self):
        print("draw your world here")
    def area(self):
        print("the area is 10412km")

a=rectanlge()
a.area()