# Password Cracker
# link: https://www.hackerrank.com/challenges/password-cracker

### Though it is listed in recursion problem but I don't think it is!

import re

def check_login_attempt(login_password):
    # taking an empty list
    result = []
    for i in password:
        # finding occurences in login_password
        # if found then add it to result list and delete from login_password
        # otherwise continue
        if login_password.find(i) > -1:
            result.append(i)
            login_password = login_password.replace(i,"")
        else:
            continue

    # checking login_password is empty or not and return result according to it
    if login_password == "":
        return result
    else:
        return False


test_case = int(input())

while test_case > 0:
    # take inputs
    no_of_users = int(input())
    password = [x for x in input().split()]
    login_password = input()

    # call function
    result = check_login_attempt(login_password)

    # processing output according to returned value
    if result == False:
        print("WRONG PASSWORD")
    else:
        # taking a list of zeros
        sort_result = [0 for x in range(len(login_password))]
        for i in result:
            # finding all occurences of a substring in a string by python regex
            search = [m.start() for m in re.finditer(i, login_password)]
            # inserting the substring/substrings according to index value
            for j in search:
                sort_result[j] = i

        # taking a list for showing output
        output = []
        # inserting value to output
        # if zero then continue, otherwise append to output list
        for i in sort_result:
            if i == 0:
                continue
            else:
                output.append(i)

        # finally, show the output
        print(" ".join(output))

    test_case = test_case - 1



### better code by other submissions
#
# # build up partial string character by character and check if partial string in part of one of the passwords
# # if yes, continue adding letters and checking
# # if not, wrong password
# # eventually if partial string matches entire password, start new partial string
# def check_login_attempt(passwordlist, attempt):
#     # partial string
#     temp = ""
#     # list of correct passwords found
#     correct_passwords = ""
#     # read in attempt letter by letter
#     for letter in attempt:
#         temp = temp + letter
#         # if the current partial string is in any of the correct passwords, continue
#         for password in passwordlist:
#             if temp in password:
#                 break
#         # if it wasn't found in any of them, wrong password
#         else:
#             print("WRONG PASSWORD")
#             return
#         # if partial string matches a full password, add it to list of correct passwords and start new partial string
#         if temp in passwordlist:
#             correct_passwords = correct_passwords + temp + " "
#             temp = ""
#     print(correct_passwords)
#
#
#
# # First line is integer T = total number of test cases then T test cases follow
# t = int(input())
# for i in range(0, t):
#     # First line of each test case contains N number of passwords
#     n = int(input())
#     # Second line has those N passwords as space-separated strings
#     passwords = input().split()
#     # Third line is login attempt
#     check_login_attempt(passwords,input())
