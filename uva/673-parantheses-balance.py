
def main():
    case = int(input())

    while case:
        string = input()
        stack = ["#"]        
        if len(string) > 0:
            stack.append(string[0])
        s = 1
        for i in range(1, len(string)):
            if (string[i] == ")" and stack[s] == "(") or (string[i] == "]" and stack[s] == "["):
                stack.pop()
                s = s - 1     
            else:
                stack.append(string[i])
                s = s + 1
        
        if len(stack) == 1:
            print("Yes")
        else :
            print("No")
        case = case - 1

main()