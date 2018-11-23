
def main():
    case = int(input())
    n = case
    while case:
        case = case - 1        
        creatures = list(map(int, input().split()))
        speed = max(creatures[1:])
        ## messed up output format in question        
        print("Case "+ str(n - case) +": "+ str(speed)) 

main()
