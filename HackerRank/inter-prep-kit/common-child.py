def commonChild(s1, s2):
    from itertools import combinations
    a = b = set()
    for i in range(len(s1)+1, 0, -1):
        a = set(combinations(s1, i))
        b = set(combinations(s2, i))
        result = a & b
        if len(result):
            return i
    return 0


print(commonChild("ASDDERF",
                  "ASWEDRT"))
