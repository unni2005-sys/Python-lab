numbers = [10, 15, 20, 25, 30, 35, 40]
new_list = []
for number in numbers:
    if number % 2 != 0:
        new_list.append(number)
print("List after removing even numbers:", new_list)
