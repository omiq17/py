while True:
    h = int(input())
    m = int(input())

    if h == 12:
        h = 0

    if m == 0:
        h = 12 - h
        print (h , m)
    else:        
        h = 11 - h
        m = 60 - m
        if h == 0:
            h = 12
        print (h , m)


        