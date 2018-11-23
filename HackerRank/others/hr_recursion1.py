## Problem Name: Recursive Digit Sum
## link: https://www.hackerrank.com/challenges/recursive-digit-sum

import math

# for finding out the sum of numbers
def count_digits(n):
    sum_of_digits = 0
    temp = 11
    i = 0

    while temp>9:
        temp = int(n/math.pow(10, i))
        sum_of_digits  += int(temp%10)
        i = i+1

    return sum_of_digits

# for finding out the super digit
# recursion function
def super_digit(sum_of_digits):
    if sum_of_digits < 10:
        return sum_of_digits
    else:
        sum_of_digits = count_digits(sum_of_digits)
        return super_digit(sum_of_digits)

# taking two inputs
n, k = map(int, input().split())

sum_of_digits = count_digits(n)

result = super_digit(sum_of_digits*k)

print(result)
