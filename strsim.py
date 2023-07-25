str1: str = input("Enter the string 1 :")
str2: str = input("Enter the string 2 :")

short = min(len(str1), len(str2))
long = max(len(str1), len(str2))

match_char: int = 0

for i in range(short):
    if str1[i] == str2[i]:
        match_char += 1
print(f"The similarity between two strings : {str1} and {str2} is {match_char / long} or {(match_char / long) * 100}%")
