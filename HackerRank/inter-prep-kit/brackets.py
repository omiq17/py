def main():
    n = int(input())

    while n!=0:
        n = n-1
        br = input()
        lbr = len(br)
        stack = []
        brdict = {'(':')', '{':'}', '[':']'}

        for i in range(lbr):
            val = br[i]            
            if val == "{" or val == "(" or val == "[":
                stack.append(val)
            else:
                if stack != []:
                    if brdict[stack.pop()] == val:
                        continue
                    else:
                        stack = ["{"]
                        break
                else:
                    stack = ["{"]
                    break
            
        if stack == []:
            print("YES")
        else:
            print("NO")

main()