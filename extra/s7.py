n = int(input())
res = [[0 for y in range(n)] for x in range(n)]
num = 1

for val in range(1,n+1):
    if val%2 == 0:
        i =  1
        j = val
        for v in range(1, val+1):
            res[i-1][j-1] = num
            num = num + 1
            i = i+1
            j = j-1
    else:
        i = val
        j = 1
        for v in range(1, val+1):
            res[i-1][j-1] = num
            num = num + 1
            i = i-1
            j = j+1


for val in range (2, n+1):
    if val%2 == 0:
            i =  val
            j = n
            for v in range(val, n+1):
                res[i-1][j-1] = num
                num = num + 1
                i = i+1
                j = j-1
    else:
        i = n
        j = val
        for v in range(val, n+1):
            res[i-1][j-1] = num
            num = num + 1
            i = i-1
            j = j+1

print(res)
        
