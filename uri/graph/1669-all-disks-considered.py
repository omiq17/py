def main():
    while 1:
        disk1, disk2, dep = map(int, input().strip().split())
        if disk1 == 0:
            break

        count = 0
        flag1 = False
        flag2 = False

        for i in range(dep):
            value1, value2 = map(int, input().strip().split())
            if value1 <= disk1 and value2 > disk1 and flag1 == False:
                count = count + 1
                flag1 = True
            elif value1 > disk1 and value2 <= disk1 and flag2 == False:
                count = count + 1
                flag2 = True
            else:
                continue

        if count == 2:
            print("4")
        else:
            print("3")


main()
