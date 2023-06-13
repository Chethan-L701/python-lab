def factorial(n: int):
    if (n <= 1):
        return 1
    return n*factorial(n-1)


num = int(input("Enter the number: "))
print("Factorial of {} is {}".format(num, factorial(num)))
