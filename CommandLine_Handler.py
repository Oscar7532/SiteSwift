import CommandLine_Output as clo
import Error_Handler as eh
def display(input):
    try:
        clo.output(input)
    except:
        eh.error("c-e20")

