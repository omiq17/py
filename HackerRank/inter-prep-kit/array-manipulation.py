n = 5
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

data = [0] * (n+1)

for si, ei, val in queries: 
    data[si-1] += val
    data[ei] -= val

print(data)

for i in range(1, n+1):
    data[i] += data[i-1]

print(data)

print(max(data))