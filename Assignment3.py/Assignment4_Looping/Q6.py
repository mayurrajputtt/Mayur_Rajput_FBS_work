# WAP to check if a given number is prime number or not.

n = int(input("Enter the number: "))


if n <= 1:
    print("Not prime")

else:
    for i in range(2 , n - 1):
        if ( n % i == 0):
            print("Not prime")
            break

    else:
        print("It is prime")


