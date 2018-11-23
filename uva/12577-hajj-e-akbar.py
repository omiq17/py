
def main():
    case = 1
    while True:
        uinput = input()
        if uinput[0] == "*":
            break
        elif uinput[0] == "H":
            print("Case " + str(case) + ": Hajj-e-Akbar")
        else:
            print("Case " + str(case) + ": Hajj-e-Asghar")
        case = case + 1

main()