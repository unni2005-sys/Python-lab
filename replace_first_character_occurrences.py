s = input("Enter a string: ")

if s:
    first_char = s[0]
    lower_char = first_char.lower()
    upper_char = first_char.upper()
    rest = s[1:].replace(lower_char, "$").replace(upper_char, "$")
    result = first_char + rest
    print("Result:", result)
else:
    print("Result:")
