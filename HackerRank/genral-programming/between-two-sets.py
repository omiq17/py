def getTotalX(a, b):
    max_a = max(a)
    upto = min(b)
    cm = set()

    for i in a:
        j = 1
        temp = set()
        while j * i <= upto:
            temp.add(j * i)
            j = j + 1
        if cm == set():
            cm = temp.copy()
        else:
            cm = cm & temp

    filt = cm.copy()
    for k in cm:
        for j in b:
            if j % k == 0:
                continue
            else:
                filt.remove(k)
                break

    return len(filt)


print (getTotalX([2, 4], [16, 32, 96]))
# print (getTotalX([5, 7], [49, 48]))
