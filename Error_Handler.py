import CommandLine_Output as cmo
def error(code):
    if code[:1]=="c-":
        match code[2:]:
            case "e20":
                cmo.output("Error - (e20): Print Error")