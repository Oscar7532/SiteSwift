import CommandLine_Output as clo
import Error_Handler as eh
def display(input):
    try:
        clo.output(input)
    except:
        eh.error("c-e20")
        
def login()
    username = admin
    password = 1234
    if username == input("Username: ") and password == input("Password: "):
        return True
    return False
    
def interface(run_Interface = True):
    while run_Interface == True:
        if login():
            clo.output("login successful")
            while run_Interface == True:
            
            
            
        