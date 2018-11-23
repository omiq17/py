from collections import OrderedDict
def main():
    cases = int(input())
    n = cases

    while cases:
        cases = cases - 1        
        sites = OrderedDict()
        max = 0

        for i in range(10):
            key, value = input().split()
            value = int(value)
            if value > max:
                max = value
                sites.clear()
                sites[key] = value
            elif value == max:
                sites[key] = value

        print("Case #" + str(n - cases) + ":")
        for i in sites:
            print(i)

main()