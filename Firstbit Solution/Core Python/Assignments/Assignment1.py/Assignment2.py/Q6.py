# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

B = int(input("Enter the Basic salary: "))

# DA = Dearness Allowence 
DA = (10 / 100) * B  

# TA = Travel Allowence
TA = (12 / 100) * B

# HRA = House Rent Allowence
HRA = (15 / 100) * B

Total_Salary = (B + DA + TA + HRA)

print(Total_Salary)