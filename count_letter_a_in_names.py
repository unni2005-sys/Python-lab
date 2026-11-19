names = input("Enter the names :").split()
count = 0
for name in names:
    for char in name:
        if char == "a":
            count = count + 1
print(count)
