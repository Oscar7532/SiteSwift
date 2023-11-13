# Startup and import
# import libraries
import threading
# import files
import CommandLine_Handler as clh
import Error_Handler as eh
import Mailbox as mb

# Startup

# Command Line
if __name__ == "__main__":
  cmdInterface = threading.Thread(target = clh.interface)
  cmdInterface.daemon = True
  cmdInterface.start()


# Run Loop
mb.run_Main = True
mb.x = 0
while mb.run_Main == True:
  mb.x += 1