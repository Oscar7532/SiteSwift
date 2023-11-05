import CommandLine_Output as clo
import Error_Handler as eh
import Mailbox as mb

def display(input):
    try:
        clo.output(str(input))
    except:
        eh.error("c-e20")
        
def login():
    username = "admin"
    password = "1234"
    userIn = clo.uInput("Username: ")
    passIn = clo.uInput("Password: ")
    if username == userIn and password == passIn:
        return True
    return False
    
def interface():
    mb.run_Interface = True
    while mb.run_Interface == True:
        login_state = login()
        if login_state == True:
            clo.output("login Successful")
            intDisplay = interfaceDisplay()
            while login_state == True and mb.run_Interface == True:
                clo.clear()
                clo.output("----Main Menu----")
                clo.output("Options:\nstate) The current state of the server.\nusers) User Management.\nsettings) Settings.\nlogout) Logout")
                valid_input = False
                while valid_input == False:
                    match clo.uInput(">->").lower():
                        case "state":
                            valid_input = True
                            intDisplay.state()
                        case "user":
                            valid_input = True
                            intDisplay.users()
                        case "settings":
                            valid_input = True
                            intDisplay.settings()
                        case "logout":
                            valid_input = True
                            login_state = False
                        case _:
                            clo.output("Option not found - Please check your spelling against listed options above to avoid grammatical errors.")
        else:
            clo.output("login Un-successful")

class interfaceDisplay():
    def __init__(self):
        self.__username = "Temp"
    def state(self):
        clo.clear()
        clo.output("State")
        clo.output("Current State - Probably Running #WIP not connected to state yet")
        runDisplayState = True
        while runDisplayState == True:
            clo.output("Options:\nreturn) Return to Main menu.")
            valid_input = False
            while valid_input == False:
                match clo.uInput(">->").lower():
                    case "return":
                        valid_input = True
                        runDisplayState = False
                    case _:
                        clo.output(
                            "Option not found - Please check your spelling against listed options above to avoid grammatical errors.")

    def users(self):
        clo.clear()
        clo.output("Users")
        clo.output("#WIP")
        runDisplayUsers = True
        while runDisplayUsers == True:
            clo.output("Options:\nreturn) Return to Main menu.")
            valid_input = False
            while valid_input == False:
                match clo.uInput(">->").lower():
                    case "return":
                        valid_input = True
                        runDisplayUsers = False
                    case _:
                        clo.output(
                            "Option not found - Please check your spelling against listed options above to avoid grammatical errors.")

    def settings(self):
        clo.clear()
        clo.output("Settings")
        clo.output("#WIP")
        runDisplaySet = True
        while runDisplaySet == True:
            clo.output("Options:\nreturn) Return to Main menu.")
            valid_input = False
            while valid_input == False:
                match clo.uInput(">->").lower():
                    case "return":
                        valid_input = True
                        runDisplaySet = False
                    case _:
                        clo.output(
                            "Option not found - Please check your spelling against listed options above to avoid grammatical errors.")