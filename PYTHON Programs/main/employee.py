class Employee:
    def __init__(self, empno, name, designation):
        self.empno = empno
        self.name = name
        self.designation = designation

class Qualification(Employee):
    def __init__(self, empno, name, designation, UGMarks, PGMarks, Experience):
        super().__init__(empno, name, designation)
        self.UGMarks = UGMarks
        self.PGMarks = PGMarks
        self.Experience = Experience

class Salary(Qualification):
    def __init__(self, empno, name, designation, UGMarks, PGMarks, Experience):
        super().__init__(empno, name, designation, UGMarks, PGMarks, Experience)
        
    def display_details(self):
        print("Employee Details:")
        print("Emp No:", self.empno)
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("UG Marks:", self.UGMarks)
        print("PG Marks:", self.PGMarks)
        print("Experience:", self.Experience)

    def compute_increment(self):
        increment = 0
        if self.Experience > 5:
            increment += 5000
        if self.UGMarks >= 75:
            increment += 3000
        if self.PGMarks >= 75:
            increment += 5000
        print("Increment Amount:", increment)

emp1 = Salary("E001", "John", "Manager", 80, 85, 6)
emp1.display_details()
emp1.compute_increment()

