#for clearing screen
import os
#for calculations
import math
#for exiting code in stop_code()
import time
#for text coloring in welcome messages
from colorama import Fore, Back, Style

#feature collects data input from user for what they want to do
feature = "undefined"
#loop cancel keeps the loop in intro() going till exited in stop_code()
loop_cancel = False

#intro() takes user input for variable: function and sends user to either history(), stop_code() or shape_select()
def intro():
  #creates global variables
  global feature
  global loop_cancel
  #begins loop in case of error
  while loop_cancel != True:
    #clears screen
    os.system("clear")
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!")
    #asks for user input and gives them their choices
    print(Style.NORMAL + "\nWhat feature would you like to use today?")
    feature = input("   • Perimeter checker \n   • Area checker \n   • History \n   • Exit \n\nPlease enter one: ").lower()
    #if feature = Perimeter, set feature to perimeter for later and send       to shape select
    if feature == "p" or feature == "perimeter" or feature == "perimeter checker" or feature == "1":
      feature = "Perimeter"
      shape_select()
    #if feature = Area, set feature to Area for later and send to shape        select
    elif feature == "a" or feature == "area" or feature == "area checker" or feature == "2":
      feature = "Area"
      shape_select()
    #if History, send to history()
    elif feature == "h" or feature == "history" or feature == "3":
      feature = "History"
      history()
    #if Exit, send to stop_code()
    elif feature == "e" or feature == "exit" or feature == "4":
      feature = "Exit"
      stop_code()
      loop_cancel = True
    #if anything else, error and return to start of loop
    else:
      input("\nUnknown response, press <enter> to restart. ")
      os.system("clear")
      intro()
  os.system("clear")

#shape_select() comes from perimeter or area in variable: function and asks for shape to calculate
def shape_select():
  os.system("clear")
  #welcomes
  print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!")
  print(Style.NORMAL + "\nWhat shape would you like to calculate?")
  shape = input("   • Rectangle/Square \n   • Circle \n   • Triangle \n   • Paralellogram  \n\nPlease enter one: ").lower()
  #if rectangle/square, clear screen, send to rectangle_square()
  if shape == "rectangle" or shape == "square" or shape == "rectangle square" or shape == "rectangle/square" or shape == "r" or shape == "s" or shape == "1":
    os.system("clear")
    rectangle_square()
  #if circle, clear screen, send to circle()
  elif shape == "circle" or shape == "c" or shape == "2":
    os.system("clear")
    circle()
  #if triangle, clear screen, send to triangle()
  elif shape == "triangle" or shape == "t" or shape == "3":
    os.system("clear")
    triangle()
  #if paralellogram, clear screen, send to paralellogram()
  elif shape == "paralellogram" or shape == "p" or shape == "4":
    os.system("clear")
    paralellogram()
  #if anything else, error and send back to intro()
  else:
    input("\nUnknown response, press <enter> to restart. ")
    #clears screen
    os.system("clear")
    intro()

#rectangle_square() holds all the math and data for rectangle/square calculations
def rectangle_square(): 
  #welcomes
  print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
  #confirms user input
  confirm = input(Style.NORMAL + "You are wanting to know the {} of your Rectangle/Square.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  #clear screen
  os.system("clear")
  #if user wants to return to start, send to intro()
  if confirm == "x":
    intro()
  #otherwise continue with code
  else:
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
    #begins a value error try: except: to create a invalid input
    try:  
      #asks for user input regarding side lengths
      base = float(input(Style.NORMAL + "Please enter the Base length of your Rectangle/Square: "))
      height = float(input("Please enter the Height of your Rectangle/Square: "))
    #if value error, send error and send user to confimation at start of rectangle_square()
    except ValueError:
      print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
      input("Press <enter> to continue. ")
      #clear screen
      os.system("clear")
      rectangle_square()

    #if 0 or negative numer inputed, error and return to confimation
    if base <= 0 or height <= 0:
      print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
      input("Press <enter> to continue")
      rectangle_square()
    #if all numbers in positives, continue
    else:
      #clear screen
      os.system("clear")
      #welcomes
      print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")

    #area math
    area = base * height
    #perimeter math
    perimeter = base + base + height + height
    #area rounded to 3dp
    roundarea = round(area, 3)
    #perimeter rounded to 3dp
    roundperimeter = round(perimeter, 3)

    #checks what feature user is using
    if feature == "Area":
      #tells user rounded answer
      print(Style.NORMAL + "Your Area of your Shape is: {} (rounded)".format(roundarea))
      #tells user how to calculate with full answer
      input("This is calculated by base({}) * height({}) = {}\n\nPress <enter> to return to menu.  ".format(base, height, area))
      #save data to saved_data.txt
      data = open("saved_data.txt", "a")
      data.write("Rectangle: Base = {}, Height = {}, Area = {}\n".format(base, height, area))
      data.close()
      os.system("clear")
      #return to start
      intro()
    #checks what feature user is using
    elif feature == "Perimeter":
      #tells user rounded answer
      print(Style.NORMAL + "Your Perimeter of your Shape is: {} (rounded)".format(roundperimeter))
      #tells user how to calculate with full answer
      input("This is calculated by (base({}) * 2) + (height({}) * 2) = {}\n\nPress <enter> to return to menu.  ".format(base, height, perimeter))
      #save data to saved_data.txt
      data = open("saved_data.txt", "a")
      data.write("Rectangle: Base = {}, Height, = {} Perimeter = {}\n".format(base, height, perimeter))
      data.close()
      #clear screen
      os.system("clear")
      #send user back to intro() when they are done
      intro()
    #if there is a error, reset code
    else:
      intro()
def circle():
  #welcomes
  print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
  #confirms user input
  confirm = input(Style.NORMAL + "You are wanting to know the {} of your Circle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  #clear screen
  os.system("clear")
  #if user wants to return to start, send to intro()
  if confirm == "x":
    intro()
  #otherwise continue with code
  else:
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
  #begins a value error try: except: to crate invalid input
  try:
    #asks for user input regarding radius of their circle
    radius = float(input(Style.NORMAL + "Please enter the Radius of your Circle: "))
  #if value error, send error and send user to confirmation at start of circle()
  except ValueError:
    print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
    input("Press <enter> to continue. ")
    #clear screen
    os.system("clear")
    circle()
  #if 0 or negative number inputted, error and returm to confimation
  if radius <= 0:
    print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
    input("Press <enter> to continue")
    circle()
  #if all numbers are in positives, continue
  else:
    #clear screen
    os.system("clear")
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")

  #area math
  ca1 = radius * radius
  area = math.pi * ca1
  #perimeter math
  perimeter = 2 * math.pi * radius
  #area rounded to 3dp
  roundarea = round(area, 3)
  #perimeter rounded to 3dp
  roundperimeter = round(perimeter, 3)
  
  #checks what feature user is using
  if feature == "Area":
    #tells user rounded answer
    print(style.NORMAL + "Your Area of your Shape is: {} (rounded)".format(roundarea))
    #tells user how to calculate with full answer
    input("This is calculated by (radius({}) * radius({})) * π = {}\n\nPress <enter> to return to menu.  ".format(radius, radius, area))
    #save data to saved_data.txt
    data = open("saved_data.txt", "a")
    data.write("Circle: Radius = {}, Area = {}\n".format(radius, area))
    data.close()
    os.system("clear")
    #return to start
    intro()
  #checks what feature user is using
  elif feature == "Perimeter":
    #tells user rounded answer
    print(Style.NORMAL + "Your Perimeter of your Shape is: {} (rounded)".format(roundperimeter))
    #tells user how to calculate with full answer
    input("This is calculated by (radius({}) * π * 2) = {}\n\nPress <enter> to return to menu.  ".format(radius, perimeter))
    #save data to saved_data.txt
    data = open("saved_data.txt", "a")
    data.write("Circle: Radius = {} Perimeter = {}\n".format(radius, perimeter))
    data.close()
    os.system("clear")
    #return to start
    intro()
  #if there is a error, reset code
  else:
    intro()

def triangle():
  #welcomes
  print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
  confirm = input(Style.NORMAL + "You are wanting to know the {} of your Triangle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  #if user wants to return to start, send to intro()
  if confirm == "x":
    #clear screen
    os.system("clear")
    intro()
  #else, continue code
  else:
    #clear screen
    os.system("clear")
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
  #begins a value error try: except: to create invalid input
  try:  
    #checks what feature user inputted
    if feature == "Area":
      #asks for user input regarding triangle height and base length
      base = float(input(Style.NORMAL + "Please enter the Base length of your Triangle: "))
      height = float(input("Please enter the Height of your triangle: "))
      
      #if inputted number is 0 or negatives, error and return to ocnfimation at start of triangle()
      if base <= 0 or height <= 0:
        print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
        input("Press <enter> to continue")
        triangle()
      #else, continue code
      else:
      
        #area math
        area = (base * height) / 2
        #area rounded to 3dp
        roundarea = round(area, 3)
      
      #clear screen
      os.system("clear")
      #welcomes
      print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
      #tells user rounded answer
      print(Style.NORMAL + "Your Area of your Shape is: {} (rounded)".format(roundarea))
      #tells user how to calculate with full answer
      input("This is calculated by (base({}) * height({})) / 2 = {}\n\nPress <enter> to return to menu.  ".format(base, height, area))
      #saves data to saved_data.txt
      data = open("saved_data.txt", "a")
      data.write("Triangle: Base = {}, Height = {}, Area = {}\n".format(base, height, area))
      data.close()
      os.system("clear")
      #sends user back to intro() when they are done
      intro()
      
    #checks what feature user is using
    elif feature == "Perimeter":
      #asks for user input regarding triangle side lengths
      side1 = float(input("Please enter the Length of Side 1: "))
      side2 = float(input("Please enter the Length of Side 2: "))
      side3 = float(input("Please enter the Length of Side 3: "))
      
      #if user input is 0 or negatives, error and return to confimation at start of triangle()
      if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
        input("Press <enter> to continue")
        triangle()
      #else, contine code
      else:
      
        #perimeter math
        perimeter = side1 + side2 + side3
        #perimeter rounded to 3dp
        roundperimeter = round(perimeter, 3)
      
      #clear screen
      os.system("clear")
      #welcomes
      print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
      #tells user rounded answer
      print(Style.NORMAL + "Your Perimeter of your Shape is: {} (rounded)".format(roundperimeter))
      #tells user how to calculate with full answer
      input("This is calculated by side1({}) + side2({}) + side3({}) = {}\n\nPress <enter> to return to menu.  ".format(side1, side2, side3, perimeter))
      #saves data to saved_data.txt
      data = open("saved_data.txt", "a")
      data.write("Triangle: Side1 = {}, Side2 = {}, Side3 = {}, Perimeter = {}\n".format(side1, side2, side3, perimeter))
      data.close()
      os.system("clear")
      #send user back to intro() when they are done
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
  #welcomes
  print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")
  #confirms users input
  confirm = input(Style.NORMAL + "You are wanting to know the {} of your Parallelogram.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  #if user wants to return to start, send to intro()
  if confirm == "x":
    #clear screen
    os.system("clear")
    intro()
  #else, continue code
  else:
    #clear screen
    os.system("clear")
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n") 
    #begins a value error try: except: to create a invalid input
    try:  
      #asks for user input regarding side lengths
      base = float(input(Style.NORMAL + "Please enter the Base length of your Rectangle/Square: "))
      side = float(input("Please enter the Height of your Rectangle/Square: "))
    #if value error, send error and send user to confimation at start of paralellogram()
    except ValueError:
      print("\nThe value you entered either doesen't exist or is not a number. Please Try again")
      input("Press <enter> to continue. ")
      #clear screen
      os.system("clear")
      rectangle_square()
    
    #if 0 or negative numer inputed, error and return to confimation
    if base <= 0 or side <= 0:
      print("\nA number you input was less than or equal to 0, please make sure all your inputs are in the positives\n")
      input("Press <enter> to continue")
      paralellogram()
    #if all numbers in positives, continue
    else:
      #clear screen
      os.system("clear")
      #welcomes
      print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!\n")

    #area math
    area = base * side
    #perimeter math
    perimeter = base + base + side + side
    #area rounded to 3dp
    roundarea = round(area, 3)
    #perimeter rounded to 3dp
    roundperimeter = round(perimeter, 3)

    #checks what feature user is using
    if feature == "Area":
      #tells user rounded answer
      print(Style.NORMAL + "Your Area of your Shape is: {} (rounded)".format(roundarea))
      #tells user how to calculate with full answer
      input("This is calculated by base({}) * side({}) = {}\n\nPress <enter> to return to menu.  ".format(base, side, area))
      #save data to saved_data.txt
      data = open("saved_data.txt", "a")
      data.write("Parallelogram: Base = {}, Side = {}, Area = {}\n".format(base, side, area))
      data.close()
      os.system("clear")
      #return to start
      intro()
    #checks what feature user is using
    elif feature == "Perimeter":
      #tells user rounded answer
      print(Style.NORMAL + "Your Perimeter of your Shape is: {} (rounded)".format(roundperimeter))
      #tells user how to calculate with full answer
      input("This is calculated by (base({}) * 2) + (side({}) * 2) = {}\n\nPress <enter> to return to menu.  ".format(base, side, perimeter))
      #save data to saved_data.txt
      data = open("saved_data.txt", "a")
      data.write("Parallelogram: Base = {}, Side = {}, Perimeter = {}\n".format(base, side, perimeter))
      data.close()
      os.system("clear")
      #return to start
      intro()
    #if there is a error, reset code
    else:
      intro()

def history():
  #opens saved_data.txt
  data = open("saved_data.txt", "r")
  data_list = data.readlines()
  data_number_check = len(data_list)
  data.close()
  #checks if there is anything in saved_data.txt
  #if there is no data, tell user and return them to intro()
  if data_number_check == 0:
    #clear screen
    os.system("clear")
    #welcome
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker! \n")
    input(Style.NORMAL + "Sorry, There seems to be no history avalible\n\n\nPress <enter> to return to main menu. ")
    intro()
  #if there is data show data
  else:
    data_set = 0
    #clear screen
    os.system("clear")
    #welcome
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!")
    print(Style.NORMAL + "\nHistory:\n")
    for i in data_list:
      print(data_list[data_set])
      data_set += 1
    input("\nPress <enter> to continue. ")
    #return to intro() when user is ready
    intro()
def stop_code():
  #opens saved_data.txt
  data = open("saved_data.txt", "r")
  data_list = data.readlines()
  data_number_check = len(data_list)
  data.close()
  #checks that there is data in saved_data.txt
  #if there is no data, exit code
  if data_number_check == 0:
    #clears screen
    os.system("clear")
    #thanks user for using code
    print(Style.DIM + "Thank you for using Fraser High School's Official Perimeter and Area Checker!")
    print(Style.NORMAL + "\nExiting...")
    time.sleep(2.5)
    os.system("clear")
  #if there is data, show data
  else:
    data_set = 0
    os.system("clear")
    #welcomes
    print(Style.DIM + "Welcome to Fraser High School's official Perimeter and Area checker!")
    print(Style.NORMAL + "\nHistory:\n")
    for i in data_list:
      print(data_list[data_set])
      data_set += 1
    input("\nPress <enter> to continue to exit. ")
    #clear screen
    os.system("clear")
    #thanks user for using code
    print(Style.DIM + "Thank you for using Fraser High School's Official Perimeter and Area Checker!")
    #exits code and breaks loop in intro() causing there to be no exit message
    print(Style.NORMAL + "\nExiting...")
    time.sleep(2.5)
    #clears screen
    os.system("clear")
#resets saved_data.txt
data = open("saved_data.txt", "w")
data.write("")
data.close()
#starts code at intro()
intro()