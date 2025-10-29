# Accept age of five people and also per person ticket amount and
# then calculate total amount to ticket to travel for all of them
# based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full.

total = 0

for i in range(1 , 6):
    print(f"\nperson{i}:")

    age = int(input("Enter the age: "))
    ticket_amount = float(input("Enter the ticket amount: "))

    if (age < 12):
        amount_to_pay = ticket_amount * 0.7

    elif(age > 59):
        amount_to_pay = ticket_amount * 0.5

    else:
        amount_to_pay = ticket_amount

total = total + amount_to_pay

print("\n--------------------------")
print("Total amount to pay for all 5 people:",total)
print("-----------------------------")  




