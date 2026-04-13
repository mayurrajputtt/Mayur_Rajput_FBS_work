# Base Class : Student

class Student:
    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Fail"

    def display(self):
        print("ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
        print("Rank:", self.calculateRank())

    def __str__(self):
        return f"{self.studentId} {self.name} {self.percentage}"