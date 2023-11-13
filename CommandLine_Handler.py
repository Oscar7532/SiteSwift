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
    passIn = clo.passInput("Password: ")
    if username == userIn and password == passIn:
        return True
    return False
    
def interface():
    mb.run_Interface = True
    while mb.run_Interface == True:
        clo.clear()
        login_state = login()
        clo.clear()
        if login_state == True:
            clo.output("login Successful")
            intDisplay = interfaceDisplay()
            while login_state == True and mb.run_Interface == True:
                clo.clear()
                clo.output("----Main Menu----")
                clo.output("Options:\nstat) The current state of the server.\nuser) User Management.\nset) Settings.\nlogout) Logout")
                valid_input = False
                while valid_input == False:
                    match clo.uInput(">->").lower():
                        case "stat":
                            valid_input = True
                            intDisplay.state()
                        case "user":
                            valid_input = True
                            intDisplay.users()
                        case "set":
                            valid_input = True
                            intDisplay.settings()
                        case "logout":
                            valid_input = True
                            login_state = False
                        case _:
                            clo.output("Option not found - Please check your spelling against listed options above to avoid grammatical errors.")
                    clo.clear()
        else:
            clo.output("login Un-successful")

class interfaceDisplay():
    def __init__(self):
        self.__username = "Temp"
    def state(self):
        clo.clear()
        clo.output("State")
        clo.output("Current State - Probably Running #WIP not connected to state yet")
        clo.output(("Current Run loop state - " + str(mb.x)))
        runDisplayState = True
        while runDisplayState == True:
            clo.output("Options:\nback) Return to Main menu.")
            valid_input = False
            while valid_input == False:
                match clo.uInput(">->").lower():
                    case "back":
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
            clo.output("Options:\nback) Return to Main menu.")
            valid_input = False
            while valid_input == False:
                match clo.uInput(">->").lower():
                    case "back":
                        valid_input = True
                        runDisplayUsers = False
                    case _:
                        clo.output(
                            "Option not found - Please check your spelling against listed options above to avoid grammatical errors.")

    def settings(self):
        clo.clear()
        clo.output("Settings")
        clo.output("Backend system settings and controls")
        runDisplaySet = True
        while runDisplaySet == True:
            clo.output("Options:\nshutdown) Shutdown whole system (DANGER: no failsafe).\nback) Return to Main menu.")
            valid_input = False
            while valid_input == False:
                match clo.uInput(">->").lower():
                    case "shutdown":
                        valid_input = True
                        mb.run_Interface = False
                        mb.run_Main = False
                        runDisplaySet = False
                        clo.clear()
                    case "back":
                        valid_input = True
                        runDisplaySet = False
                    case _:
                        clo.output(
                            "Option not found - Please check your spelling against listed options above to avoid grammatical errors.")