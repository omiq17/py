def countSwaps(li):
    n = len(li)
    count = 0

    # from last go to first
    for i in range(n, 1, -1):
        # initializing the checking element
        check = li[0]
        swaped = False
        # from first go to i'th value
        for j in range(1, i):
            # if check element is grater, then swap elements
            # if equal, then do nothing
            # otherwise update check elements
            if check > li[j]:
                li[j-1], li[j] = li[j], li[j-1]
                swaped = True
                count = count + 1
            elif check == li[j]:
                continue
            else:
                check = li[j]
        if swaped == False:
            break

    print("Array is sorted in " + str(count)+ " swaps.")
    print("First Element: "+ str(li[0]))
    print("Last Element: "+ str(li[-1]))

def main():
    #converting list int elements to str
    li = [int(x) for x in input("Give the numbers to be sorted "+
            "(separated by space): ").split()]
    # li = [2, 5,1,7,-33, -2, -999, 434, 4 ,24, 432]
    countSwaps(li)

main()