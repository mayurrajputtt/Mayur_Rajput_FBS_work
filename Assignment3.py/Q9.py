# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

math = int(input("Enter the marks of math: "))
bio = int(input("Enter the marks of bio: "))
marathi = int(input("Enter the marks of marathi: "))
hindi = int(input("Enter the marks of hindi: "))
english = int(input("Enter the marks of english: "))

total_marks = math + bio + marathi + hindi + english
print(f"Total marks:  {total_marks}")

percentage = (total_marks / 500) * 100
print(f"Percentage: {percentage}")

if (percentage > 60):
    print("First Class")

elif( 45< percentage < 60):
    print("Second class")

elif(35 < percentage < 45):
    print("Pass Class")

else:
    print("Fail")





