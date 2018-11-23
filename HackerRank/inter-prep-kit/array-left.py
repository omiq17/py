def rotateLeft(d, arr):
    for i in range(d):
        temp = arr[0]
        del arr[0]
        arr.append(temp)

    return arr


def main():
    a, d = map( int, input().split() )
    # print(a, d)

    arr = list(map(int, input().split()))
    # print(arr)

    result = rotateLeft (d, arr)
    print(" ".join(str(i) for i in result))

main()



