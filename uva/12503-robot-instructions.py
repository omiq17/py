def main():
    case = int(input().strip())
    while case:
        n = int(input().strip())
        
        instructions = []
        pos = 0
        for i in range(n):
            rule = input().strip()
            if rule == "LEFT":
                instructions.append(-1)
            elif rule == "RIGHT":
                instructions.append(1)
            else:
                k = int(rule.split()[-1])
                instructions.append(instructions[k-1])
            pos = pos + instructions[i]
        
        print(pos)
        case = case - 1

main()