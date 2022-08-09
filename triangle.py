import math

a = 0
b = 0
c = 0

a = int(input("Side 1 (not base): "))
c = int(input("Side 2 (not base): "))
b = int(input("Base Length: "))
print("Triangle Height")
h = int(input("set to '0' if right angled triangle: "))


perimeter = a + b + c
area = (h * b) / 2

if area == 0:
  print("\nThis data is incorrect to there is insufficent data to conclude a area")
else:
  print("\nThe area of the triangle is", area)
print("The perimeter of the triangle is", perimeter)