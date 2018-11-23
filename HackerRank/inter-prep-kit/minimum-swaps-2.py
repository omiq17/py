arr = [4,3,1,2]
# arr_copy = list(arr)

# n = len(arr)
# swap_front = 0
# swap_back = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#             swap_front = swap_front + 1

# for i in range(n-1, 0, -1):
#     for j in range(0, i):
#         # print(i,j)
#         if arr_copy[i] < arr_copy[j]:
#             arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
#             swap_back = swap_back + 1

# print(swap_front if swap_front < swap_back else swap_back)



n = len(arr)
c = 0
for i in range(0, n-1):
    while (i+1) != arr[i]:
        key = arr[i] -1
        arr[i], arr[key] = arr[key], arr[i]
        c = c+1

print(arr, c)