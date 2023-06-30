import re


def find_pattern(text: str) -> (list, list):
    phone_match = re.findall("\+91[0-9]{10}", text)
    email_id_match = re.findall("\S+@\S+\.\S+", text)
    return phone_match, email_id_match


input_text = str(input("Enter the text to search for phone no and email id : "))
print(find_pattern(input_text))
