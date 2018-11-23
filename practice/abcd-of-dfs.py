# ## UVA 459 graph connectivity Stack
# # import sys
# from functools import lru_cache
# # sys.setrecursionlimit(10000000)
#
## @lru_cache(maxsize=100000)
## def dfs(node, visit, graph):
##    stack = [node]
##     while stack:
##         vertex = stack.pop()
##         if visit[vertex] == 0:
##             visit[vertex] = 1
##             stack.extend(graph[vertex])
##     return 0
#
# def main():
#     case = int(input().strip())
#     input()
#     while case > 0:
#         case = case - 1
#         nodes = ord(input().strip()) - 64
#         graph = dict([(k,[]) for k in range(nodes+1)])
#         visit = [0] * (nodes+1)
#         subgraph = 0
#
#         while True:
#             edge x= input().strip()
#             if edge == '':
#                 break
#             else:
#                 value1 = ord(edge[0]) - 64
#                 value2 = ord(edge[1]) - 64
#                 graph[value1].append(value2)
#                 graph[value2].append(value1)
#
#         for i in range(1,nodes+1):
#             if visit[i] == 0:
#                 stack = [i]
#                 while stack:
#                     vertex = stack.pop()
#                     if visit[vertex] == 0:
#                         visit[vertex] = 1
#                         stack.extend(graph[vertex])
#                 subgraph = subgraph + 1
#
#         print(subgraph)
#         if case > 0:
#             print()
#
#     return 0
#
# main()
#
### UVA 459 graph connectivity with recursion
def main():
    case = int(input().strip())
    input()
    while case > 0:
        case = case - 1
        nodes = ord(input().strip()) - 64
        graph = [[] for x in range(nodes+1)]
        visit = [0 for x in range(nodes+1)]
        subgraph = 0

        while True:
            try:
                edge = input().strip()
            except(EOFError):
                break
            if edge == '':
                break
            else:
                value1 = ord(edge[0]) - 64
                value2 = ord(edge[1]) - 64
                graph[value1].append(value2)
                graph[value2].append(value1)

        def dfs(node):
            visit[node] = 1
            for i in graph[node]:
                if visit[i] == 0:
                    dfs(i)
            return 0

        for i in range(1,nodes+1):
            if visit[i] == 0:
                dfs(i)
                subgraph = subgraph + 1

        print(subgraph)
        if case > 0:
            print()

    return 0

main()
#
# ### UVA p11518 c dominos
# case = int(input())
#
# while case > 0:
#     case = case - 1
#     totalDominos, falls, sources = map(int, input().split())
#     dominos = [[] for i in range(totalDominos+1)]
#     visit = [0 for i in range(totalDominos+1)]
#
#     for i in range(falls):
#         a, b = map(int, input().split())
#         dominos[a].append(b)
#
#     start = []
#     for i in range(sources):
#         start.append(int(input()))
#
#     # print(dominos, start)
#     totalFalls = 0
#
#     def dfs(i):
#         count = 0
#         if visit[i] == 0:
#             count = count + 1
#             visit[i] = 1
#
#         for x in dominos[i]:
#             if visit[x] == 0:
#                 visit[x] = 1
#                 count = count + 1
#                 count = count + dfs(x)
#             else:
#                 continue
#
#         return count
#
#     for i in start:
#         totalFalls = totalFalls + dfs(i)
#
#     print(totalFalls)
####################################################################
# ### UVA p784 Maze Exploration
# case = int(input())
# while case > 0:
#     case = case - 1
#     maze = []
#
#     j = 0
#     while True:
#         line = input()
#         maze.append([])
#
#         for i in line:
#             if i == "*":
#                 sourceC = line.index(i)
#                 sourceR = j
#             maze[j].append(i)
#
#         if line != "" and line[0] == "_":
#             break
#         j = j + 1
#
#     # rowList = [-1, 0, 0, 1]
#     # colList = [0, -1, 1, 0]
#
#     def dfs(i,j):
#         rowList = [-1, 0, 0, 1]
#         colList = [0, -1, 1, 0]
#         for k in range(4):
#             if maze[i+rowList[k]][j+colList[k]] == " ":
#                 maze[i+rowList[k]][j+colList[k]] = "#"
#                 dfs(i+rowList[k], j+colList[k])
#
#
#     # print(maze)
#     wall = maze[0][0]
#     maze[sourceR][sourceC] = "#"
#     dfs(sourceR, sourceC)
#
#     for i in range(len(maze)):
#         for j in maze[i]:
#             print(j, end="")
#         print()
#
#######################################################################
### UVA p572: oilDeposits
# while True:
#     row, col = map(int, input().split())
#     if row == 0:
#         break
#     matrix = [[0 for x in range(col+2)] for x in range(row+2)]
#
#     for i in range(row):
#         value = input()
#         for j in range(col):
#             if value[j] == "@":
#                 matrix[i+1][j+1] = 1
#
#     # print("Graph Representation: ",matrix)
#
#     def dfs(adjacentList):
#         for i in adjacentList[0]:
#             for j in adjacentList[1]:
#                 if matrix[i][j] == 1:
#                     matrix[i][j] = 2
#                     dfs([[i-1, i, i+1], [j-1, j, j+1]])
#
#     oilDeposits = 0
#     for i in range(row):
#         for j in range(col):
#             if matrix[i+1][j+1] == 1:
#                 matrix[i+1][j+1] = 2
#                 # res = dfs([[i, i+1, i+2], [j, j+1, j+2]])
#                 # print(res)
#                 dfs([[i, i+1, i+2], [j, j+1, j+2]])
#                 oilDeposits = oilDeposits + 1
#
#     print(oilDeposits)
