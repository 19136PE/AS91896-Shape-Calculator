import os
import math
import time
import colorama

feature = "undefined"
loop_cancel = False

#add rounding!!!

def intro():
  global feature
  global loop_cancel
  while loop_cancel != True:
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker! \n\nWhat feature would you like to use today?")
    feature = input("   • Perimeter checker \n   • Area checker \n   • History \n   • Exit \n\nPlease enter one: ").lower()
    if feature == "p" or feature == "perimeter" or feature == "perimeter checker" or feature == "1":
      feature = "Perimeter"
      shape_select()
    elif feature == "a" or feature == "area" or feature == "area checker" or feature == "2":
      feature = "Area"
      shape_select()
    elif feature == "h" or feature == "history" or feature == "3":
      feature = "History"
      history()
    elif feature == "e" or feature == "exit" or feature == "4":
      feature = "Exit"
      stop_code()
      loop_cancel = True
    else:
      input("\nUnknown response, press <enter> to restart. ")
      os.system("clear")
      intro()
  os.system("clear")
    
def shape_select():
  os.system("clear")
  print("Welcome to Fraser High School's official Perimeter and Area checker! \n\nWhat shape would you like to calculate?")
  shape = input("   • Rectangle/Square \n   • Circle \n   • Triangle \n   • Paralellogram  \n\nPlease enter one: ").lower()
  if shape == "rectangle" or shape == "square" or shape == "rectangle square" or shape == "rectangle/square" or shape == "r" or shape == "s" or shape == "1":
      
    os.system("clear")
    rectangle_square()
  elif shape == "circle" or shape == "c" or shape == "2":
    
    os.system("clear")
    circle()
  elif shape == "triangle" or shape == "t" or shape == "3":
    
    os.system("clear")
    triangle()
  elif shape == "paralellogram" or shape == "p" or shape == "4":
    
    os.system("clear")
    paralellogram()
  else:
    input("\nUnknown response, press <enter> to restart. ")
    
    os.system("clear")
def rectangle_square(): 
  print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
  confirm = input("You are wanting to know the {} of your Rectangle/Square.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  
  os.system("clear")
  if confirm == "x":
    intro()
  else:
    print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
    try:  
      base = float(input("Please enter the Base length of your Rectangle/Square: "))
      height = float(input("Please enter the Height of your Rectangle/Square: "))
    except ValueError:
      print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
      input("Press <enter> to continue. ")
      os.system("clear")
      rectangle_square()

    if base <= 0 or height <= 0:
      print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
      input("Press <enter> to continue")
      rectangle_square()
    else:
      os.system("clear")
      print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
      
    area = base * height
    perimeter = base + base + height + height

    if feature == "Area":
      input("Your Area of your Shape is: {}".format(area))
      input("This is calculated by base({}) * height({}) = {}\n\nPress <enter> to return to menu.  ".format(base, height, area))
      data = open("saved_data.txt", "a")
      data.write("Rectangle: Base = {}, Height = {}, Area = {}\n".format(base, height, area))
      data.close()
      os.system("clear")
      intro()
    elif feature == "Perimeter":
      print("Your Perimeter of your Shape is: {}".format(perimeter))
      input("This is calculated by (base({}) * 2) + (height({}) * 2) = {}\n\nPress <enter> to return to menu.  ".format(base, height, perimeter))
      data = open("saved_data.txt", "a")
      data.write("Rectangle: Base = {}, Height, = {} Perimeter = {}\n".format(base, height, perimeter))
      data.close()
      os.system("clear")
      intro()
    else:
      intro()
def circle():
  print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
  confirm = input("You are wanting to know the {} of your Circle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  os.system("clear")
  if confirm == "x":
    intro()
  else:
    print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
  try:
    radius = float(input("Please enter the Radius of your Circle: "))
  except ValueError:
    print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
    input("Press <enter> to continue. ")
    os.system("clear")
    circle()
  if radius <= 0:
    print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
    input("Press <enter> to continue")
    circle()
  else:
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker!\n")

  ca1 = radius * radius
  area = math.pi * ca1

  perimeter = 2 * math.pi * radius
  
  if feature == "Area":
    print("Your Area of your Shape is: {}".format(area))
    input("This is calculated by (radius({}) * radius({})) * π = {}\n\nPress <enter> to return to menu.  ".format(radius, radius, area))
    data = open("saved_data.txt", "a")
    data.write("Circle: Radius = {}, Area = {}\n".format(radius, area))
    data.close()
    os.system("clear")
    intro()
  elif feature == "Perimeter":
    print("Your Perimeter of your Shape is: {}".format(perimeter))
    input("This is calculated by (radius({}) * π * 2) = {}\n\nPress <enter> to return to menu.  ".format(radius, perimeter))
    data = open("saved_data.txt", "a")
    data.write("Circle: Radius = {} Perimeter = {}\n".format(radius, perimeter))
    data.close()
    os.system("clear")
    intro()
  else:
    intro()

def triangle():
  print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
  confirm = input("You are wanting to know the {} of your Triangle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  if confirm == "x":
    os.system("clear")
    intro()
  else:
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
  try:  
    if feature == "Area":
      base = float(input("Please enter the Base length of your Triangle: "))
      height = float(input("Please enter the Height of your triangle: "))
      
      if base <= 0 or height <= 0:
        print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
        input("Press <enter> to continue")
        triangle()
      else:
      
        area = (base * height) / 2
      
      os.system("clear")
      print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
      print("Your Area of your Shape is: {}".format(area))
      input("This is calculated by (base({}) * height({})) / 2 = {}\n\nPress <enter> to return to menu.  ".format(base, height, area))
      data = open("saved_data.txt", "a")
      data.write("Triangle: Base = {}, Height = {}, Area = {}\n".format(base, height, area))
      data.close()
      os.system("clear")
      intro()
      
    elif feature == "Perimeter":
      side1 = float(input("Please enter the Length of Side 1: "))
      side2 = float(input("Please enter the Length of Side 2: "))
      side3 = float(input("Please enter the Length of Side 3: "))
      if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
        input("Press <enter> to continue")
        triangle()
      else:
      
        perimeter = side1 + side2 + side3
      
      os.system("clear")
      print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
      print("Your Perimeter of your Shape is: {}".format(perimeter))
      input("This is calculated by side1({}) + side2({}) + side3({}) = {}\n\nPress <enter> to return to menu.  ".format(side1, side2, side3, perimeter))
      data = open("saved_data.txt", "a")
      data.write("Triangle: Side1 = {}, Side2 = {}, Side3 = {}, Perimeter = {}\n".format(side1, side2, side3, perimeter))
      data.close()
      os.system("clear")
      intro()
      
    else:
      input("There was an error getting this data, Press <enter> to Continue. ")
      triangle()
  except ValueError:
    print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
    input("Press <enter> to continue. ")
    os.system("clear")
    triangle()

def paralellogram():
  print("Welcome to Fraser High School's official Perimeter and Area checker!\n")
  confirm = input("You are wanting to know the {} of your Parallelogram.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  if confirm == "x":
    os.system("clear")
    intro()
  else:
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker!\n") 
    try:  
      base = float(input("Please enter the Base length of your Rectangle/Square: "))
      side = float(input("Please enter the Height of your Rectangle/Square: "))
    except ValueError:
      print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
      input("Press <enter> to continue. ")
      os.system("clear")
      rectangle_square()
    
    if base <= 0 or side <= 0:
      print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
      input("Press <enter> to continue")
      paralellogram()
    else:
      os.system("clear")
      print("Welcome to Fraser High School's official Perimeter and Area checker!\n")

    area = base * side
    perimeter = base + base + side + side

    if feature == "Area":
      print("Your Area of your Shape is: {}".format(area))
      input("This is calculated by base({}) * side({}) = {}\n\nPress <enter> to return to menu.  ".format(base, side, area))
      data = open("saved_data.txt", "a")
      data.write("Parallelogram: Base = {}, Side = {}, Area = {}\n".format(base, side, area))
      data.close()
      os.system("clear")
      intro()
    elif feature == "Perimeter":
      print("Your Perimeter of your Shape is: {}".format(perimeter))
      input("This is calculated by (base({}) * 2) + (side({}) * 2) = {}\n\nPress <enter> to return to menu.  ".format(base, side, perimeter))
      data = open("saved_data.txt", "a")
      data.write("Parallelogram: Base = {}, Side = {}, Perimeter = {}\n".format(base, side, perimeter))
      data.close()
      os.system("clear")
      intro()
    else:
      intro()

def history():
  data = open("saved_data.txt", "r")
  data_list = data.readlines()
  data_number_check = len(data_list)
  data.close()
  if data_number_check == 0:
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker! \n")
    input("Sorry, There seems to be no history avalible\n\n\nPress <enter> to return to main menu. ")
    intro()
  else:
    data_set = 0
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker! \n\nHistory:\n")
    for i in data_list:
      print(data_list[data_set])
      data_set += 1
    input("\nPress <enter> to continue. ")
    intro()
def stop_code():
  data = open("saved_data.txt", "r")
  data_list = data.readlines()
  data_number_check = len(data_list)
  data.close()
  if data_number_check == 0:
    os.system("clear")
    print("Thank you for using Fraser High School's Official Perimeter and Area Checker!")
    print("\nExiting...")
    time.sleep(2.5)
    os.system("clear")
  else:
    data_set = 0
    os.system("clear")
    print("Welcome to Fraser High School's official Perimeter and Area checker! \n\nHistory:\n")
    for i in data_list:
      print(data_list[data_set])
      data_set += 1
    input("\nPress <enter> to continue to exit. ")
    os.system("clear")
    print("Thank you for using Fraser High School's Official Perimeter and Area Checker!")
    print("\nExiting...")
    time.sleep(2.5)
    os.system("clear")
data = open("saved_data.txt", "w")
data.write("")
data.close()
intro()