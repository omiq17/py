def substrCount(n, s):
    c = len(s)
    l = c

    for i in range(l-1):
        j = 1
        while True:
            try:
                if s[i-j: i] == s[i+1: i+1+j] and i-j > -1:
                    c = c+1
                else:
                    break
                j = j + 1
            except IndexError:
                break

        k = 1
        while True:
            # print(i, k)
            if s[i] == s[i+k]:
                if k % 2 != 0:
                    c = c+1
            else:
                break
            k = k+1
            if i+k == l:
                break

    return c


print(substrCount(4, "abcbaba"))
