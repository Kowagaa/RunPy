import os
file = open("code.py", "w")
ask = input("Type ONE python line of code ")
run = " "
file.write(ask)
run = input("Do yo want to run it? (y or n)? ")
while True:
  while run == "n":
    print(" ")
    ask = input("Type ONE python line of code: ")
    file.write(ask)
    run = input("Do yo want to run it? (y or n)? ")
    os.system("clear")
  while run == "y":
    os.system("clear")
    os.system("python code.py")
    run = input("Do yo want to run it? (y or n)? ")

