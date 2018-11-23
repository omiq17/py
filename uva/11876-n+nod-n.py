##########################################
### This solution has NOT ACCEPTED
### Got TIME LIMIT
### Create a pull request if you have solved it 
##########################################

from math import sqrt
def main():
    case = int(input())
    n = case

    def countDivisors(num):
        count = 0
        j = int(sqrt(num)) + 1
        for i in range(1, j):
            if num%i == 0:
                if num/i == i:
                    count = count + 1
                else:
                    count = count + 2

        return count
    
    nod_seq = [1]
    nod = 1
    while nod<=1000000:
        temp = nod + countDivisors(nod)
        nod_seq.append(temp)
        nod = temp


    while case:
        case = case - 1        
        a, b = map(int, input().split())
        while True:
            try:
                a = nod_seq.index(a)
                break
            except(ValueError):
                a = a + 1
        while True:
            try:
                b = nod_seq.index(b)
                break
            except(ValueError):
                b = b - 1

        print("Case " + str(n-case) + ": " + str(b - a + 1 ))        

main()