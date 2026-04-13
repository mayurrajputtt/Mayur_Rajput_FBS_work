# Derived Class : EnggStudent

class EnggStudent(Student):
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self, studentId, name, age, percentage, branch, internalMarks):
        super().accept(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def calculateRank(self):
        total = self.percentage + (self.internalMarks / 2)
        if total >= 80:
            return "Excellent"
        elif total >= 60:
            return "Good"
        else:
            return "Average"

    def display(self):
        super().display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internalMarks)

    def __str__(self):
        return f"{self.name} {self.branch} {self.internalMarks}"
