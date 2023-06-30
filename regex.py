import re


def is_phone_number_no_regex(num: str) -> bool:
    if num[3] == num[7] == "-" and len(num) == 12:
        num = num[:3] + num[4:7] + num[8:]
        if num.isdigit():
            print("It is a phone no.")
            return True
    print("It is not a phone number")
    return False


def is_phone_number_with_regex(num: str):
    match = re.search("^[0-9]{3}-[0-9]{3}-[0-9]{4}$", num)
    if match is not None:
        print(match)
        print("It is a phone no.")
        return True
    print("It is not a phone number")
    return False
