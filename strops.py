input_text = str(input("Enter the text: "))

nupper = nlower = ndigits = 0

for ch in input_text:
    if ch.isdigit():
        ndigits += 1
    elif ch.islower():
        nlower += 1
    elif ch.isupper():
        nupper += 1

print(
    f"No of :\nwords : {len(input_text.split())}\ncharacter : {len(input_text)}\nnumerical digits : {ndigits}\nuppercase char : {nupper}\nlowercase char : {nlower}")
