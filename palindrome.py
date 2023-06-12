data = str(input("Enter the number or string to check for palindrome : "))
if data == data[::-1]:
    print("Enter number or string is a palindrome.")
else:
    print("The given number or string is not palindrome.")
times = {}
for c in data:
    if c in times:
        times[c] += 1
    else:
        times[c] = 1

for key in times:
    print("{} : {}".format(key, times[key]))
