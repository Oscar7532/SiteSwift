import os
def output(input):
    print(input)
def uInput(prompt):
    userInput = input(prompt)
    return userInput
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    #os.system("cls")