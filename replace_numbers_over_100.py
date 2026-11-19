nums = list(map(int, input("Enter the integers : ").split()))
result = []
for number in nums:
    if number > 100:
        result.append("Over")
    else:
        result.append(number)
print("Result =", result)
