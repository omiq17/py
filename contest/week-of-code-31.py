### Colliding Circles
pi = 3.141592653589793


###############################################################
### Zero-One-Game
# games = int(input())
# while games > 0:
#     games = games - 1
#     length = int(input())
#     sequence = list(map(int, input().split()))
#     loop = 0
#     consecutiveZeroes = 0
#
#     for i in range(length):
#         if sequence[i] == 0:
#             consecutiveZeroes = consecutiveZeroes + 1
#             if consecutiveZeroes >= 3:
#                 loop = loop + 1
#         elif sequence[i] == 1 and (i == length-1 or i == 0):
#             continue
#         elif sequence[i-1] == 0 and sequence[i] == 1 and sequence[i+1] == 0:
#             consecutiveZeroes = consecutiveZeroes + 1
#             if consecutiveZeroes >= 3:
#                 loop = loop + 1
#         else:
#             consecutiveZeroes = 0
#
#     print("loop", loop)
#     if loop % 2 == 0:
#         print("Bob")
#     else:
#         print("Alice")
#
# ### Accurate Sorting
# case = int(input())
# while case > 0:
#     length = int(input())
#     numbers = list(map(int, input().split()))
#
#     for i in range(length-1):
#         if numbers[i] - 1 == numbers[i+1]:
#             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#
#     flag = True
#     for i in range(length-1):
#         if numbers[i] + 1 != numbers[i+1]:
#             flag = False
#             break
#
#     if flag:
#         print("Yes")
#     else:
#         print("No")
#
#     case = case - 1
#
##################################################
# ### Beautiful World
# word = input()
#
# previous = ""
# vowels = "aeiouy"
# vowelsFlag = False
# flag = True
#
# for i in range(len(word)):
#     temp = word[i] in vowels
#     if word[i] == previous:
#         flag = False
#         break
#     elif vowelsFlag and temp:
#         flag = False
#         break
#     vowelsFlag = temp
#     previous = word[i]
#
# if flag:
#     print("Yes")
# else:
#     print("No")
