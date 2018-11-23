
def main():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))

    for i  in arr[d:]:
        print(i, end=" ")

    for i in arr[:d]:
        print(i, end=" ")

    # print (' '.join(str(i) for i in arr) )
    
main()