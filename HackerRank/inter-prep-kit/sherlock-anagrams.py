def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s)):
        for p in range(len(s)-i):
            a = dict()
            for m in range(p, p+i):
                try:
                    a[s[m]] = a[s[m]] + 1
                except KeyError:
                    a[s[m]] = 1

            for j in range(p, len(s)-i):
                b = dict()
                for m in range(j+1, j+1+i):
                    try:
                        b[s[m]] = b[s[m]] + 1
                    except KeyError:
                        b[s[m]] = 1
                    # print(s[m])
                # print(a, b)
                if a == b:
                    count = count + 1

    return count


print(sherlockAndAnagrams("abcd"))
