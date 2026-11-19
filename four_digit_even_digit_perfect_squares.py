import math

start = int(input("Enter a starting range in 4 digits: "))
end = int(input("Enter an ending range in 4 digits: "))

if 1000 <= start <= 9999 and 1000 <= end <= 9999:
    result = []
    for i in range(start, end + 1):
        if all(int(digit) % 2 == 0 for digit in str(i)):
            root = math.isqrt(i)
            if root * root == i:
                result.append(i)
    print("The list of perfect square numbers are:", result)
else:
    print("Please enter valid 4-digit numbers.")
