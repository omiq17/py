import sys
sys.setrecursionlimit(10000000)
def main():
    global maxDepth
    while 1:
        flag = False
        row, col = map(int, input().split())
        graph = [[2 for x in range(col+2)] for x in range(row+2)]
        if row == 0:
            break

        for i in range(row):
            value = input()
            for j in range(col):
                if value[j] == ".":
                    graph[i+1][j+1] = 0
                    if flag == False:
                        flag = True
                        sourceR = i + 1
                        sourceC = j + 1
                else:
                    graph[i+1][j+1] = 1


        def dfs(i, j, depth):
            global maxDepth, childC, childR
            visit[i][j] = 1
            # count = 0
            rowList = [-1, 0, 0, 1]
            colList = [0, -1, 1, 0]
            for k in range(4):
                r = i+rowList[k]
                c = j+colList[k]
                if graph[r][c] == 0 and visit[r][c] == 0:
                    dfs(r, c, depth + 1)

            if depth > maxDepth:
                maxDepth = depth
                childR = i
                childC = j

            visit[i][j] = 0
            return

        visit = [[0 for x in range(col+2)] for x in range(row+2)]
        dfs(sourceR, sourceC, 0)
        # visit = [[0 for x in range(col+2)] for x in range(row+2)
        maxDepth = 0
        dfs(childR, childC, 0)
        # print(childR, childC)
        print(maxDepth)

maxDepth = 0
childC = 0
childR = 0
main()
