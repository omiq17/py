#################################################
# 1081: DFSr - Depth hierarchy
def main():
    case = int(input())
    caseNo = 1

    while case:
        nodes, edges = map(int, input().split())
        graph = dict( [(k,[]) for k in range(nodes)] )
        for i in range(edges):
            edge1, edge2 = map(int, input().split())
            graph[edge1].append(edge2)

        for i in graph:
            graph[i].sort()
        # print(graph)

        print("Caso " + str(caseNo) + ":")
        visit = [0] * (nodes)

        def dfs(node, level):
            visit[node] = 1
            flag = False

            for j in graph[node]:
                for i in range(level):
                    print(" ", end = "")
                if visit[j] == 0:
                    if not flag:
                        flag = True
                    print(str(node)+ "-" +str(j)+ " pathR(G," +str(j)+ ")")
                    dfs(j, level+2)
                else:
                    print(str(node)+ "-" +str(j))

            return flag

        for i in range(nodes):
            if visit[i] == 0:
                flag = dfs(i, 2)
                if flag:
                    print()

        case = case - 1
        caseNo = caseNo + 1

main()
