
# def main():
#     def minimumNumber(n, password):
#         numbers = "0123456789"
#         lower_case = "abcdefghijklmnopqrstuvwxyz"
#         upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         special_characters = "!@#$%^&*()-+"

#         if n == 0:
#             return 6

#         condition = 0
#         for  value in password:
#             # print(value)
#             if value in numbers:
#                 numbers = ""
#                 condition = condition + 1
#             elif value in lower_case:
#                 lower_case = ""
#                 condition = condition + 1
#             elif value in upper_case:
#                 upper_case = ""
#                 condition = condition + 1
#             elif value in special_characters:
#                 special_characters = ""
#                 condition = condition + 1

#         if condition == 4:
#             if n < 6:
#                 return 6-n
#             else:
#                 return 0
#         else:
#             condition = 4 - condition
#             if n + condition < 6:
#                 condition = condition + (6 - n - condition)
#             return condition

#     n = int(input().strip())
#     password = input().strip()
#     answer = minimumNumber(n, password)
#     print(answer)

# main()

######################################################

def main():
    

main()