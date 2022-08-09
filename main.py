import os
import math
import time
import turtle

feature = "undefined"

def intro():
  global feature
  while True:
    print("Welcome to Fraser High Schools official Perimeter and Area checker \n\nWhat feature would you like to use today?")
    feature = input("   • Perimeter checker \n   • Area checker \n\nPlease enter one: ").lower()
    if feature == "p" or feature == "perimeter" or feature == "perimeter checker" or feature == "1":
      feature = "Perimeter"
    elif feature == "a" or feature == "area" or feature == "area checker" or feature == "2":
      feature = "Area"
    else:
      print("\nUnknown response, please try again.")
      time.sleep(1)
      os.system("clear")
      intro()
      
    time.sleep(1)
    os.system("clear")
    print("Welcome to Fraser High Schools official Perimeter and Area checker \n\nWhat shape would you like to calculate?")
    shape = input("   • Rectangle/Square \n   • Circle \n   • Triangle \n   • Paralellogram  \n\nPlease enter one: ").lower()
    if shape == "rectangle" or shape == "square" or shape == "rectangle square" or shape == "rectangle/square" or shape == "r" or shape == "s" or shape == "1":
      time.sleep(1)
      os.system("clear")
      rectangle_square()
    elif shape == "circle" or shape == "c" or shape == "2":
      time.sleep(1)
      os.system("clear")
      circle()
    elif shape == "triangle" or shape == "t" or shape == "3":
      time.sleep(1)
      os.system("clear")
      triangle()
    elif shape == "paralellogram" or shape == "p" or shape == "4":
      time.sleep(1)
      os.system("clear")
      paralellogram()
    else:
      print("\nUnknown response, please try again.")
      time.sleep(1)
      os.system("clear")


def rectangle_square(): 
  print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
  confirm = input("You are wanting to know the {} of your Rectangle/Square.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  time.sleep(1)
  os.system("clear")
  if confirm == "x":
    intro()
  else:
    print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
    try:  
      length = float(input("Please enter the Base length of your Rectangle/Square: "))
      height = float(input("Please enter the Height of your Rectangle/Square: "))
    except ValueError:
      print("The value you entered either doesen't exist or is not a number. Please Try again")
      time.sleep(3)
      os.system("clear")
      rectangle_square()
    time.sleep(1)
    os.system("clear")
    print("Welcome to Fraser High Schools official Perimeter and Area checker\n")

    area = length * height
    perimeter = length + length + height + height

    if feature == "Area":
      input("Your Area of your Shape is: {}\n\nPress <enter> to return to menu ".format(area))
      os.system("clear")
      intro()
    elif feature == "Perimeter":
      input("Your Perimeter of your Shape is: {}\n\nPress <enter> to return to menu ".format(perimeter))
      os.system("clear")
      intro()
    else:
      intro()

def circle():
  print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
  confirm = input("You are wanting to know the {} of your Circle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  time.sleep(1)
  os.system("clear")
  if confirm == "x":
    intro()
  else:
    print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
try:  
      radius = float(input("Please enter the Radius of your Circle: "))
    except ValueError:
      print("The value you entered either doesen't exist or is not a number. Please Try again")
      time.sleep(3)
      os.system("clear")
      circle()
    time.sleep(1)
    os.system("clear")
    print("Welcome to Fraser High Schools official Perimeter and Area checker\n")

    ca1 = radius * radius
    area = math.pi * ca1

    perimeter = 2 * math.pi * radius

    if feature == "Area":
      input("Your Area of your Shape is: {}\n\nPress <enter> to return to menu ".format(area))
      os.system("clear")
      intro()
    elif feature == "Perimeter":
      input("Your Perimeter of your Shape is: {}\n\nPress <enter> to return to menu ".format(perimeter))
      os.system("clear")
      intro()
    else:
      intro()

def circle():
  print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
  confirm = input("You are wanting to know the {} of your Circle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  time.sleep(1)
  os.system("clear")
  if confirm == "x":
    intro()
  else:
    print("Welcome to Fraser High Schools official Perimeter and Area checker\n")


def triangle():
  print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
  confirm = input("You are wanting to know the {} of your Triangle.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  if confirm == "x":
    intro()
  else:
    print("triangle")
    input()


def paralellogram():
  print("Welcome to Fraser High Schools official Perimeter and Area checker\n")
  confirm = input("You are wanting to know the {} of your Paralellogram.\n\n   Press enter to confirm\n   Enter 'x' to change your inputs\n   ".format(feature)).lower()
  if confirm == "x":
    intro()
  else:
    print("pawawellogwam")
    input()


intro()