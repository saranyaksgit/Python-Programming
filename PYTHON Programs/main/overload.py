class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()
# create two Rectangle objects
r1 = Rectangle(3, 4)
r2 = Rectangle(2, 5)

# compare the areas of the two rectangles using the < operator overload
if r1 < r2:
    print("The area of rectangle 1 is less than the area of rectangle 2")
else:
    print("The area of rectangle 1 is greater than or equal to the area of rectangle 2")

