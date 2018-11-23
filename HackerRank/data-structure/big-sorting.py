# def quickSort(i, n, val, li):
#     midIndex = int((i+n)/2) 
#     mid = li[midIndex]

#     if i == n:
#         if li[n] > val:
#             li.insert(n, val)
#         else:
#             li.insert(n+1, val)
#         return
#     if val == mid:
#         li.insert(midIndex, val)
#         return
#     elif val<mid:
#         quickSort(i, midIndex, val, li)
#         return
#     else:
#         quickSort(midIndex+1, n, val, li)
#         return

def main():
    n = int(input())
    li = []

    ### my solution, NOT accepted
    # for i in range(n):
    #     m = int(input())
    #     if i>1:
    #         quickSort(0, i-1, m, li)
    #     elif i==0:
    #         li.append(m)
    #     else:
    #         if m<li[0]:
    #             li.insert(0, m)
    #         else:
    #             li.append(m)

    # print("\n".join(str(i) for i in li)) 

    ### 
    # converting to int -> str is costly
    # thus optimizing the convertions
    ###
    for i in range(n):
        m = input()
        li.append(m)
    
    li.sort(key=int)
    for s in li:
        print(s)


main()