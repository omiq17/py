### HourRank 18
# Super Six Substrings
# https://www.hackerrank.com/contests/hourrank-18/challenges/super-six-substrings

s = input().strip()

n = len(s)
count = 0
for i in range(n):
    for j in range(n-i):
        val = s[j:j+i+1]
        value = int(val)
        if val[0]=="0":
            if len(val)==1:
                count = count+1
            else:
                continue
        elif value%6==0:
            count = count+1

print (count)

#got time limit error!
