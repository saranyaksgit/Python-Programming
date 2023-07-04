class Student:
    def __init__(self):
        self.rollno = ""
        self.mark1 = 0
        self.mark2 = 0
        self.total = 0

    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        self.total = self.mark1 + self.mark2

    def printDetails(self):
        print("Student details:")
        print("Roll No:", self.rollno)
        print("Mark 1:", self.mark1)
        print("Mark 2:", self.mark2)
        print("Total:", self.total)

# Example usage:
s1 = Student()
s1.readData

