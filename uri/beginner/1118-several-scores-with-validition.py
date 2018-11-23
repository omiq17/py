def main():
    valid = []
    option = False
    flag = False

    while 1:
        value = float(input())
        if option == True:
            if value == 1:
                option = False
                continue
            elif value ==  2:
                break
            else:
                print("novo calculo (1-sim 2-nao)")
                continue

        if value >= 0 and value <= 10:
            valid.append(value)
            if len(valid) == 2:
                avg = (valid[0] + valid[1]) / 2
                print("media =", "{0:.2f}".format(avg))
                valid.clear()
                print("novo calculo (1-sim 2-nao)")
                option = True
        else:
            print("nota invalida")

main()
