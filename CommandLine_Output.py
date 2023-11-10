import os
import pwinput as pIN
def output(input):
    print(input)
def uInput(prompt):
    userInput = input(prompt)
    return userInput
def passInput(prompt):
  userInput = pIN.pwinput(prompt=prompt, mask = '*')
  return userInput

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    #os.system("cls")