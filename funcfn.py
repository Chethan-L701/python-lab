def f(N: int) -> int:
    if N <= 1:
        return N
    return f(N-1)+f(N-2)


num = int(input("Enter the number: "))
print("The fibonacci number is: ", f(num))
