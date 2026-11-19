color_list1 = ["red", "green", "blue", "yellow"]
color_list2 = ["green", "yellow", "black"]

print("Colors in color-list1 not contained in color-list2:")
for color in color_list1:
    if color not in color_list2:
        print(color)
