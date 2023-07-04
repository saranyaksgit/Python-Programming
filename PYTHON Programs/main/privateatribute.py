class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary # Private attribute with double underscores

    def get_salary(self):
        return self.__salary

# Create a Teacher object and test accessing the salary attribute
teacher = Teacher("John Doe", 35, 50000)
#print(teacher.__salary) # This will raise an AttributeError
print("Teacher's salary:", teacher.get_salary())

