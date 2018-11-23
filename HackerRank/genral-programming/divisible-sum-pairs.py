def main():
    n, k = map(int, input().split())
    numbers  = list(map(int, input().split()))
    # print(numbers)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            # print(numbers[i] + numbers[j]/k)
            if (numbers[i] + numbers[j]) % k == 0:
                count = count + 1 

    print(count)

main()

### well done! same as editorial!