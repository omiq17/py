# ## J- Easy odd sum
# def main():
#     numOne, numTwo = map(int, input().split())
#
#     if numOne%2 == 0:
#         numOne = numOne + 1
#     if numTwo%2 == 1:
#         numTwo = numTwo + 1
#
#     sum = 0
#     for i in range(numOne, numTwo, 2):
#         sum = sum + i
#
#     print(sum)
#
# main()

# ###################################################################
# # ### SPOJ: LASTSHOT
# # import sys
# from functools import lru_cache
# # sys.setrecursionlimit(10000000)
#
# def main():
#     bombs, relations = map(int, input().split())
#     graph = [[] for i in range(bombs+1)]
#
#     for i in range(relations):
#         bomb1, bomb2 = map(int, input().split())
#         graph[bomb1].append(bomb2)
#     # print(graph)
#
#     @lru_cache(maxsize=1024)
#         if len(graph[bomb]) > 0:
#     def dfs(bomb):
#         count = 1
#         visit[bomb] = 1
#             for i in graph[bomb]:
#                 if visit[i] == 0:
#                     count = count + dfs(i)
#
#         return count
#
#     # @lru_cache(maxsize=100000)
#     # def dfs(node):
#     #     count = 0
#     #     stack = [node]
#     #     while stack:
#     #         vertex = stack.pop()
#     #         if visit[vertex] == 0:
#     #             visit[vertex] = 1
#     #             count = count + 1
#     #             stack.extend(graph[vertex])
#     #     return count
#
#     maxImpact = 0
#     for i in range(1, bombs+1):
#         visit = [0 for i in range(bombs+1)]
#         impact = dfs(i)
#         if impact > maxImpact:
#             maxImpact = impact
#
#     print(maxImpact)
#
# main()
###############################################################
### SPOJ: LASTSHOT recursion
import sys
sys.setrecursionlimit(1000000000000)
def main():
    bombs, relations = map(int, input().split())
    graph = [[] for i in range(bombs+1)]

    for i in range(relations):
        try:
            bomb1, bomb2 = map(int, input().split())
        except (EOFError):
            break
        graph[bomb1].append(bomb2)
    # print(graph)
    def dfs(bomb):
        count = 1
        visit[bomb] = 1
        if len(graph[bomb]) > 0:
            for i in graph[bomb]:
                if visit[i] == 0:
                    count = count + dfs(i)

        return count

    maxImpact = 0
    for i in range(1, bombs+1):
        visit = [0 for i in range(bombs+1)]
        impact = dfs(i)
        if impact > maxImpact:
            maxImpact = impact

    print(maxImpact)

main()
###################################################################
### SPOJ: LASTSHOT
### Tried with dp but failed!
# def dfs(bomb, visit, save, graph):
#     print(save)
#     visit[bomb] = 1
#     graph[bomb] = list(set(graph[bomb]))
#     max = 0
#     for i in graph[bomb]:
#         if visit[i] == 0:
#             count = dfs(i, visit, save, graph)
#         else:
#             count = save[i]
#         if count > max:
#             max = count
#
#     save[bomb] = max + 1
#     return save[bomb]
#
# def main():
#     bombs, relations = map(int, input().split())
#     graph = [[] for i in range(bombs+1)]
#
#     for i in range(relations):
#         bomb1, bomb2 = map(int, input().split())
#         graph[bomb1].append(bomb2)
#
#     # print(graph)
#
#     maxImpact = 0
#     save = [0 for i in range(bombs+1)]
#     for i in range(1, bombs+1):
#         visit = [0] * (bombs+1)
#         if save[i] != 0:
#             impact = save[i]
#         else:
#             impact = dfs(i, visit, save, graph)
#
#         if impact > maxImpact:
#             maxImpact = impact
#
#     print(maxImpact)
#     # print(save)
#
# main()
