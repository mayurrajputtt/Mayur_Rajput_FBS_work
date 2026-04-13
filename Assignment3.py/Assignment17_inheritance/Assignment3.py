# Derived Class : MedicalStudent

class MedicalStudent(Student):
    def __init__(self, studentId, name, age, percentage, specialization, internshipMarks):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.internshipMarks = internshipMarks

    def accept(self, studentId, name, age, percentage, specialization, internshipMarks):
        super().accept(studentId, name, age, percentage)
        self.specialization = specialization
        self.internshipMarks = internshipMarks

    def calculateRank(self):
        total = self.percentage + (self.internshipMarks / 2)
        if total >= 85:
            return "Top Medical Student"
        elif total >= 65:
            return "Qualified"
        else:
            return "Needs Improvement"

    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Internship Marks:", self.internshipMarks)

    def __str__(self):
        return f"{self.name} {self.specialization}"
