# # ::::::::::::::::::::::::::::::::::::::::::::::::::
# # ::::::::::::::::::::::::::::::::::::::::::::::::::
# # ::: Deteministic Finite Automaton
# #
# def checkState(current, i):
#     if(i!="a" and i!="b" and i!="c"):
#         return 5
#     if(current == 0):
#         if(i == "a"):
#             return 0
#         elif(i == "b"):
#             return 0
#         elif(i == "c"):
#             return 1
#     elif(current == 1):
#         if(i == "a"):
#             return 2
#         elif(i == "b"):
#             return 0
#         elif(i == "c"):
#             return 1
#     elif(current == 2):
#         if(i == "a"):
#             return 0
#         elif(i == "b"):
#             return 3
#         elif(i == "c"):
#             return 1
#     elif(current == 3):
#         if(i == "a"):
#             return 0
#         elif(i == "b"):
#             return 0
#         elif(i == "c"):
#             return 1
#
# while True:
#     currentState = 0
#     sentence = input()
#     if(sentence == "end"):
#         break
#
#     for i in sentence:
#         currentState = checkState(currentState, i)
#         if(currentState == 5):
#             break
#
#     if(currentState == 3):
#         print("Accepted")
#     else:
#         print("Rejected")
#
# ::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::
# ::: Find Out First 99 Palindromes
#
# def makeReverse(i):
# 	rev = 0
# 	while(i>0):
# 		rem = i%10
# 		rev = (rev*10)+rem
# 		i = i//10
# 	return rev
#
# li = []
# count = 0
#
# for i in range(999999):
# 	r = makeReverse(i)
# 	print (i,r)
# 	if(i==r):
# 		li = li + [i]
# 		count = count+1
# 	if(count==99):
# 	    break
#
# print (li)
