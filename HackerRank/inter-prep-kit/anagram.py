def main():
    line1 = input()
    line2 = list(input())
    l2 = len(line2)
    l1 = len(line1)

    count = 0
    for i in range(l1):
        word = line1[i]
        if word in line2:
            count += 1
            line2.remove(word)

    result = (l1-count) + (l2-count)

    print(result)

main()
