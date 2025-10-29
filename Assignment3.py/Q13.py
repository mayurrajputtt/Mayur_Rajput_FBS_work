# Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

# Program to calculate electricity bill

# Step 1: Input units consumed
units = int(input("Enter total units consumed: "))

# Step 2: Initialize total bill
total_bill = 0

# Step 3: Apply conditions based on units
if units <= 50:
    total_bill = units * 0.50

elif units <= 150:
    total_bill = 50 * 0.50 + (units - 50) * 0.75

elif units <= 250:
    total_bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20

else:
    total_bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

# Step 4: Add 20% surcharge
surcharge = total_bill * 0.20
total_bill = total_bill + surcharge

# Step 5: Display the result
print("Total Electricity Bill = Rs.", total_bill)
