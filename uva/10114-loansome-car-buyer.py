
def main():
    while True:
        mon, dp, loan, n = map(float, input().split())
        if mon < 0:
            break

        depr = {}
        for i in range(int(n)):
            uinput = list(map(float, input().split()))
            depr[uinput[0]] = uinput[1]

        rate = depr[0]
        price = dp + loan
        price = price - (price * rate)        
        payment = loan/mon
        months = 0

        while price < loan:
            months = months + 1            
            try:
                rate = depr[months]
            except (KeyError):
                pass
            
            price = price - (price * rate)
            loan = loan - payment

        ### Using if and for loop is an inefficient way...        
        # if price > loan:
        #     print("0 months")
        #     continue

        # for i in range(1, 1000000):
        #     try:
        #         rate = depr[i]
        #     except (KeyError):
        #         pass

        #     price = price - (price * rate)
        #     loan = loan - payment
        #     months = months + 1
            
        #     if loan < price:
        #         break

        if months == 1:
            print("1 month")            
        else:
            print(str(months) + " months")

main()