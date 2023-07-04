class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def __lt__(self, other):
        return self.area() < other.area()

# example usage
rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 8)

print(rect1.area())  # output: 50
print(rect2.perimeter())  # output: 30

if rect1 < rect2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller area")

