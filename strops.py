text = str(input("Enter the text: "))


def count_digits(text):
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    return count


def count_uppercase(text):
    count = 0
    for i in text:
        if i.isupper():
            count += 1
    return count


def count_lowercase(text):
    count = 0
    for i in text:
        if i.islower():
            count += 1
    return count


print("The number of words in the text is: ", len(text.split()))
print("The number of characters in the text is: ", len(text))
print("The number of digits in the text is: ", count_digits(text))
print("The number of uppercase letters in the text is: ",
      count_uppercase(text))
print("The number of lowercase letters in the text is: ",
      count_lowercase(text))
