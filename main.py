# Startup and import
# import libraries
from multiprocessing import Process
# import files
import CommandLine_Handler as clh
import Error_Handler as eh
import Mailbox as mb

# Startup

# Command Line
if __name__ == "__main__":
  cmdInterface = Process(target = clh.interface)
  cmdInterface.start()


# Run Loop
mb.run_Main = True
mb.x = 0
while mb.run_Main == True:
  mb.x += 1