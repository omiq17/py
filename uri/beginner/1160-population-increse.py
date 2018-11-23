import math

def main():
    case = int(input())
    while case:
        case = case - 1
        pa, pb, ga, gb = map(float, input().split())

        # if gb == 0:
        #     g = (pb-pa)*100
        #     ans = g/(pa*ga)
        #     ans = int(ans + 1)
        # else:
        #     g = (100+ga)/(100+gb)
        #     x2 = math.log(g)
        #     p = pb/pa
        #     x1 = math.log(p)
        #     try:
        #         ans = int(x1/x2)+1
        #     except(ZeroDivisionError):
        #         ans = 1
        #
        years = 0
        while True:
            pa = math.floor(pa + ((pa * ga) / 100))
            pb = math.floor(pb + ((pb * gb) / 100))
            years = years + 1
            if pa > pb or years > 100:
                break

        if years <= 100:
            print(years, "anos.")
        else:
            print("Mais de 1 seculo.")

main()
