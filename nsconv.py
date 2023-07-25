def binary_to_decimal(n: int) -> int:
    decimal = 0
    i = 0
    while n > 0:
        num = n % 10
        if num not in [0, 1]:
            print("Invalid input")
            return -1
        decimal += (num) * (2 ** i)
        n //= 10
        i += 1
    return decimal


def octal_to_decimal(n):
    decimal = 0
    i = 0
    while n > 0:
        num = n % 10
        if num not in [0, 1, 2, 3, 4, 5, 6, 7]:
            print("Invalid input")
            return -1
        decimal += (num) * (8 ** i)
        n //= 10
        i += 1
    return decimal


def octal_to_hexa(n):
    dec = octal_to_decimal(n)
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    hex = ""
    while dec > 0:
        hex = str(li[dec % 16]) + hex
        dec = dec // 16
    return hex

bin = int(input("Enter the binary number : "));
print(f"The binary number {bin} = {binary_to_decimal(bin)} in decimal system.")

oct = int(input("Enter the octal number :"))
print(f"The octal number {oct} = {octal_to_decimal(oct)} in decimals = {octal_to_hexa(oct)} in hexadecimal")
