# WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
divisor = int(input("Enter the divisor number: "))

for i in range(start, end +1):
    if i % divisor == 0:
        print(i)



