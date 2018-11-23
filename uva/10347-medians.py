from functools import reduce
from math import sqrt

def main():
    while True:
        try:
            medians = list(map(float, input().split()))            
            sm =  reduce((lambda x,y: x+y), medians)
            sm = sm/2

            try:
                area = (4/3) * sqrt(sm * (sm - medians[0]) * (sm - medians[1]) * (sm - medians[2]))
                if area < 0.1: ## take care of smallest issues...
                    print("-1.000")
                else: 
                    print("{0:.3f}".format(area))
                
            except (ValueError):
                print("-1.000")

        except (EOFError):
            break

main()