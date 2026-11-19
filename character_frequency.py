str1 = input("Enter a string: ")
freq = {}
for char in str1:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("\nCharacter frequency:")
for char in freq:
    print(char, ":", freq[char])
