# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.   

n = int(input("Enter the number of student: "))

percentage = []

for i in range(n):
    print(f"Enter the marks of student:{i+1}")
    total = 0

    for j in range(5):
        mark = float(int(input(f"Enter the marks of subject:{j+1}:")))
        total += mark

    per = (total / 500) * 100
    percentage.append(per)

print("percerntage of all student: ")
for i in range(n):
    print(f"student{i+1}: {percentage[i]} %")

average = sum(percentage)/n
print("Average percenrtage of all student,",average)

