# Assignment 1 Question:

# Take marks of 5 subjects
m1 = int(input("Enter marks of subject1:"))
m2 = int(input("Enter marks of subject2:"))
m3 = int(input("Enter marks of subject3:"))
m4 = int(input("Enter marks of subject4:"))
m5 = int(input("Enter marks of subject5:"))

# Operation performance
gain_marks = m1+ m2+ m3+ m4+ m5
percentage = (gain_marks / 500) * 100

# Display the result
print(f"percentage is {percentage} %")