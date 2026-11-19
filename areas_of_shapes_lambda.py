square = lambda side: side * side
rectangle = lambda length, breadth: length * breadth
triangle = lambda base, height: 0.5 * base * height

side = int(input("Enter side of square: "))
print("Area of square =", square(side))

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
print("Area of rectangle =", rectangle(length, breadth))

base = int(input("Enter base of triangle: "))
height = int(input("Enter height of triangle: "))
print("Area of triangle =", triangle(base, height))
