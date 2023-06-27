data = str(input("Enter the number or string to check for palindrome : "))

# Checking if the reverse of the string is equal to the string
# data[::-1] mean from first index to last index but in the reverse , since step is -1.
if data == data[::-1]:
    print("Entered number or string is a palindrome.")
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
