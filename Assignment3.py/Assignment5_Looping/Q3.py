# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passengers = int(input("Enter the number of Pasenger: "))
tickit_cost = int(input("Enter the cost of Tickit: "))

total_amount = 0 

for i in range(1, passengers+1):
    age = int(input("Enter the age of pasengers: "))

    if(age < 12):
        amount = tickit_cost * 0.70
    
    elif(age > 59):
        amount = tickit_cost * 0.50

    else: 
        amount = tickit_cost

    total_amount += amount

print(total_amount)


