def main():
    while 1:
        try:
            valueOne, valueTwo = map(int, input().split())
        except (EOFError):
            break
        valueOne = "{0:{fill}32b}".format(valueOne, fill="0")
        valueTwo = "{0:{fill}32b}".format(valueTwo, fill="0")
        # print(valueOne)
        result = ""

        for i in range(32):
            if valueOne[i] == "1" and valueTwo[i] == "1":
                result += "0"
            elif valueOne[i] == "0" and valueTwo[i] == "0":
                result += "0"
            else:
                result += "1"

        print(int(result, 2))

main()
