#############################################################
### 1087 Queen
def main():
    while 1:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0:
            break

        xDiff = abs(x1 - x2)
        yDiff = abs(y1 - y2)

        if xDiff == 0 and yDiff == 0:
            print("0")
        elif xDiff == yDiff:
            print("1")
        elif xDiff == 0 or yDiff == 0:
            print("1")
        else:
            print("2")

main()
