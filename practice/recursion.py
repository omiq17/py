### Problem 20
# def towerOfHanoi(disks, source, dest, aux):
#     if disks == 1:
#         return print(source + ' => ' + dest)
#
#     towerOfHanoi(disks-1, source, aux, dest)
#     print(source + ' => ' + dest)
#     towerOfHanoi(disks-1, aux, dest, source)
#
# disks = int(input())
# towerOfHanoi(disks, 'a', 'c', 'b')
#
###############################################################
### Problem 19
# def inOrderFibonacci(length):
#     if length == 1:
#         print("1", end=" ")
#         return
#     elif length == 2:
#         print("2", end=" ")
#         return
#
#     inOrderFibonacci(length-2)
#     print(length, end=" ")
#     inOrderFibonacci(length-1)
#     return
#
# def preOrderFibonacci(length):
#     if length == 1:
#         print("1", end=" ")
#         return
#     elif length == 2:
#         print("2", end=" ")
#         return
#
#     print(length, end=" ")
#     preOrderFibonacci(length-2)
#     preOrderFibonacci(length-1)
#     return
#
# def postOrderFibonacci(length):
#     if length == 1:
#         print("1", end=" ")
#         return
#     elif length == 2:
#         print("2", end=" ")
#         return
#
#     postOrderFibonacci(length-2)
#     postOrderFibonacci(length-1)
#     print(length, end=" ")
#     return
#
# length = int(input())
# print("Inorder Sequence: ")
# inOrderFibonacci(length)
# print()
# print("Postrder Sequence: ")
# postOrderFibonacci(length)
# print()
# print("Preorder Sequence: ")
# preOrderFibonacci(length)
# print()
###############################################################
### Problem 18
# def doStringConcatenation(first_word, second_word, start_length, end_length):
#     if start_length == end_length:
#         return second_word
#
#     return first_word[start_length] \
#             + doStringConcatenation(first_word, second_word, start_length+1, end_length)
#
#
# def doStringCopy(word, length):
#     if length == -1:
#         return ""
#     return doStringCopy(word, length-1) + word[length]
#
# def findStringLength(word, length, count):
#     if word[length] == " ":
#         return count
#
#     return findStringLength(word, length+1, count+1)
#
# def doStringCompare(first_word, second_word, length):
#     if first_word[length] == " ":
#         print("Compare String: Matched")
#         return
#     elif first_word[length] == second_word[length]:
#         doStringCompare(first_word, second_word, length+1)
#     else:
#         print("Compare String: Not Matched.")
#         return
#
# first_word = input()
# second_word = input()
#
# first_word_length =  len(first_word)
# second_word_length = len(second_word)
#
# print("Concatenation String:" , doStringConcatenation(first_word, second_word, 0, first_word_length))
# print("Copy String: ", doStringCopy(first_word, first_word_length-1))
# print("String Length: ", findStringLength(first_word+" ", 0, 0))
# doStringCompare(first_word+" ", second_word, 0)

################################################################
# ### Problem 17
# # the code is only valid for a word
# def checkPalindrome(word, start_length, end_length):
#     if start_length+1 >= end_length:
#         if word[start_length] == word[end_length]:
#             print("Palindrome")
#             return
#         else:
#             print("Not Palindrome")
#             return
#     elif word[start_length] == word[end_length]:
#         checkPalindrome(word, start_length+1,end_length-1)
#     else:
#         print("Not Palindrome")
#         return False
#
# while True:
#     word = input()
#     length = len(word)
#
#     checkPalindrome(word, 0, length-1)
#
#################################################################
# ### Problem 16
# def printRecursively(word, length = 0):
#     if word[length] == " ":
#         return
#
#     printRecursively(word, length+1)
#     print(word[length], end="")
#     return
#
# word = input()
# printRecursively(word+" ")
#
##################################################################
# ### Problem 15
# def findReverse(number, reverse_number):
#     if number == 0:
#         print(reverse_number)
#         return 1
#
#     remainder = number%10
#     number = int(number/10)
#     reverse_number = reverse_number*10 + remainder
#
#     findReverse(number, reverse_number)
#
# number = int(input())
# findReverse(number, 0)
#
######################################################################
# # ### Problem 14
# def recursive_binary(numbers, firstIndex, secondIndex, search):
#     #when it comes to last element check here
#     if firstIndex >= secondIndex:
#         return -1
#
#     #divide the list
#     div = int((secondIndex+firstIndex) / 2)
#     #comparing with search elemment
#     if(numbers[div] == search):
#         return div
#     elif(numbers[div]<search):
#         #slicing the list [startIndex:endIndex]
#         return recursive_binary(numbers, div+1, secondIndex, search)
#     else:
#         return recursive_binary(numbers, firstIndex, div-1, search)
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
# find_numbers_length = int(input())
# find_numbers = [int(x) for x in input().split()]
#
# i = 0
# while i<find_numbers_length:
#     result = recursive_binary(numbers, 0, length-1, find_numbers[i])
#     if result<0:
#         print("not found")
#     else:
#         print(result)
#     i = i+1
#
###############################################################
# ### Problem 13
# def recursive_linear(numbers, length, search):
#     if length == 0:
#         return -1
#     elif search == numbers[length-1]:
#         return length-1
#     return recursive_linear(numbers, length-1, search)
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
# find_numbers_length = int(input())
# find_numbers = [int(x) for x in input().split()]
#
# i = 0
# while i<find_numbers_length:
#     result = recursive_linear(numbers, length, find_numbers[i])
#     if result<0:
#         print("not found")
#     else:
#         print(result)
#     i = i+1
#
##############################################################
#
# ### Problem 12
# def findSecondMax(numbers, length, max, sec_max):
#     if length == 0:
#         return sec_max
#
#     temp = numbers[length]
#     if max < temp:
#         sec_max = max
#         max = temp
#     elif sec_max < temp:
#         sec_max = temp
#     return findSecondMax(numbers, length-1, max, sec_max)
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
# if numbers[length-2] > numbers[length-1]:
#     print(findSecondMax(numbers, length-3, numbers[length-2], numbers[length-1]))
# else:
#     print(findSecondMax(numbers, length-3, numbers[length-1], numbers[length-2]))
#
####################################################
#
# ### Problem 11
# def findMax(numbers, length, max):
#     if length == 0:
#         return max
#
#     temp = numbers[length-1]
#     if max < temp:
#         max = temp
#     return findMax(numbers, length-1, max)
#
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
# print(findMax(numbers, length-1, numbers[length-1]))
#
##################################################
#
### Problem 10
# def findLcm(number_a, number_b, count):
#     rem_a = number_a%count
#     rem_b = number_b%count
#
#     if rem_a!=0 and rem_b!=0:
#         return findLcm(number_a, number_b, count+1)
#     else:
#         if rem_a==0:
#             number_a = int(number_a/count)
#         if rem_b==0:
#             number_b = int(number_b/count)
#         if number_a==1 and number_b==1:
#             return count
#         else:
#             return count * findLcm(number_a, number_b, count+1)
#
# while True:
#     number_a, number_b = map(int, input().split())
#     print(findLcm(number_a, number_b, 1))
#
###################################################
#
# ### Problem 9
# def findGcd(number_a, number_b):
#     remainder = number_b%number_a
#     if  remainder == 0:
#         return number_a
#     else:
#         return findGcd(remainder, number_a)
#
# number_a, number_b = map(int, input().split())
# # swapping number if number_a > number_b
# temp = number_a
# number_a = number_b if number_a > number_b else number_a
# number_b = temp if temp > number_b else number_b
# print(findGcd(number_a, number_b))
#
# ### Problem 08
# import math
# def checkPrime(number, root):
#     if root == 1:
#         return 1
#     elif number%root == 0:
#         return 0
#     else:
#         return checkPrime(number, root-1)
#
# while True:
#     number = int(input())
#     root = int(math.sqrt(number))
#     result = checkPrime(number, root)
#
#     if result == 1:
#         print('Prime')
#     else:
#         print('Not Prime')
#
# ### Problem 07
# def findFibonacci(length):
#     if length == 1:
#         return 1
#     elif length == 2:
#         return 1
#
#     return findFibonacci(length-1) + findFibonacci(length-2)
#
# length = int(input())
# print(findFibonacci(length))
#
### Problem 06
# def findFactorial(length):
#     if length == 1:
#         return 1
#     factorial = 1
#     return factorial * length * findFactorial(length -1)
#
# length = int(input())
# print(findFactorial(length))
#
# # ### Problem 05
# import math
#
# def calculateSumOfSeries(length, x):
#     if length==0:
#         return 0
#
#     sum = 0 + math.pow(x,length-1) + calculateSumOfSeries(length-1, x)
#     return sum
#
# x_value, length = map(int, input().split())
#
# print(int(calculateSumOfSeries(length, x_value)))
#
# ### Problem 04
# def printSeries(length):
#     if length==1:
#         print("1", end=" ")
#         return
#     elif length==2:
#         printSeries(length-1)
#         print(" + x", end=" ")
#         return
#
#     printSeries(length-1)
#     print( " + " + "x^" + str(length-1), end=" ")
#
# length = int(input())
#
# printSeries(length)
#
# ### Problem 03
# #
# def printAllEvenIntegers(length):
#     if length==-1:
#         return
#     if numbers[length-1]%2 == 1:
#         del numbers[length-1]
#     printAllEvenIntegers(length-1)
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
#
### Problem 03
# printAllEvenIntegers(length)
#
# print(' '.join(str(i) for i in numbers))
#
#
# def printAllEvenIntegers(length):
#     if length==-1:
#         return
#     if numbers[length-1]%2 == 1:
#         del numbers[length-1]
#     printAllEvenIntegers(length-1)
#
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
#
# printAllEvenIntegers(length)
#
# print(' '.join(str(i) for i in numbers))
#
# ### Problem 02
#
# def printInOrder(numbers, length_now):
#     if(length-length_now > length_now-1):
#         return
#
#     print(numbers[length-length_now], numbers[length_now-1])
#     printInOrder(numbers, length_now-1)
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
#
# printInOrder(numbers, length)

# ### Problem 01
#
# def printReverseOrder(numbers,length):
#     if length == 0:
#         return True
#     print (numbers[length-1], end = " ")
#     printReverseOrder(numbers,length-1)
#
# length = int(input())
# numbers = [int(x) for x in input().split()]
#
# printReverseOrder(numbers, length)
