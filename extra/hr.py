# ::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::
### sWaP CasE
# i = input()
# swap = list(map( lambda x: x.lower() if x.isupper() else x.upper(), i))
# result = ''.join(swap)
# print (result)

# ::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::
### finding the percentage

# import functools
#
# n = int(input())
# student_marks = {}
#
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     scores = float( functools.reduce( (lambda x,y: x+y), scores )/len(scores) )
#     student_marks[name] = scores
#
# query = input()
#
# print("%.2f" % student_marks[query])

# :::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::
### LIst Comprehenssion

# x = int(raw_input())
# y = int(raw_input())
# z = int(raw_input())
# n = int(raw_input())
#
# xarr = [i for i in range(x+1)]
# yarr = [i for i in range(y+1)]
# zarr = [i for i in range(z+1)]
# # print xarr
# # result = []
# # for i in xarr:
# #     for j in yarr:
# #         for k in zarr:
# #             if (i+j+k) != n :
# #                 # print j
# #                 arr = [i,j,k]
# #                 result.append(arr)
#
# result = [[i,j,k] for i in xarr for j in yarr for k in zarr if (i+j+k) != n]
# print result

#--Best practice
# a, b, c, n = [int(raw_input()) for _ in xrange(4)]
# print [[x,y,z] for x in xrange(a + 1) for y in xrange(b + 1) for z in xrange(c + 1) if x + y + z != n]

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
## # Tuple hash code

# n = raw_input()
# s = raw_input()
# integer_list = map(int, s.split())
# t = tuple(integer_list)
# print hash(t)

#-- best practice
# n = raw_input()
# print hash(tuple([int(i) for i in raw_input().split()]))

# 23.12.2016
