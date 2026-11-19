a = list(map(int, input("Enter the integers of a : ").split()))
b = list(map(int, input("Enter the integers of b : ").split()))

if len(a) == len(b):
    print("Both have same length")
else:
    print("Both have different lengths")

if sum(a) == sum(b):
    print("Both have same sum")
else:
    print("Both have different sum")

common_elements = list(set(a) & set(b))
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found")
