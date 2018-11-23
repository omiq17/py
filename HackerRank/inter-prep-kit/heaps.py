def main():
    n = int(input())

    arr = []

    for i in range(n):
        item = int(input())
        arr.append(item)
        heapInsert(i, arr)

        print(arr)

        

def heapInsert(i, arr):
    while(i>0):
        pi = int((i-1)/2)
        if arr[pi] > arr[i]:
            arr[pi], arr[i] = arr[i], arr[pi]
            i = pi
        else:
            break

main()