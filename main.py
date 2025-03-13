import os
yes_or_no_dict = {"y" : True, "n" : False,}
def newLine():
  global yes_or_no_dict
  if yes_or_no_dict[input("New Line? [y/n] :\n").lower()]:
    open("code.py", 'w').write(input("Input ONE python line of code: \n"))
  if yes_or_no_dict[input("Run? [y/n] :\n").lower()]:
    os.system("python code.py")
while newLine() != "exit":
  os.system("clear")