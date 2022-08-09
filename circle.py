import math
radius = 0
print("please enter the radius of your circle")
radius = int(input())

ca1 = radius * radius
area = math.pi * ca1

perimeter = 2 * math.pi * radius

print("Area =", area)
print("Perimeter =", perimeter)