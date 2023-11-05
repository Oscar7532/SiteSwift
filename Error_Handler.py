import CommandLine_Output as clo
eMessage = "No error code match"

def error(code):
    if code[:1]=="c-":
        match code[2:]:
            case "e20":
                eMessage = "Print Error"
    clo.output(str("Error -",code[2:], eMessage))