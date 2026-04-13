# 4. Armstrong Number

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for i in range(start, end + 1):
    total = 0
    temp = i 
    digits = len(str(i))

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == i:
        print(i)