def main():
    case = int(input())
    caseNo = 1
    while case > 0:
        nodes, edges = map(int, input().split())
        graph = [[] for x in range(nodes+1)]
        visit = [0 for x in range(nodes+1)]
        subgraph = 0

        for i in range(edges):
            value1, value2 = input().split()
            value1 = ord(value1) - 96
            value2 = ord(value2) - 96
            graph[value1].append(value2)
            graph[value2].append(value1)

        print("Case #" + str(caseNo) + ":")
        caseNo = caseNo + 1

        def dfs(node):
            visit[node] = 1
            for i in graph[node]:
                if visit[i] == 0:
                    component.append(i)
                    dfs(i)
            return

        for i in range(1, nodes+1):
            component = [i]
            if visit[i] == 0:
                dfs(i)
                subgraph = subgraph + 1
                component.sort()
                for j in component:
                    print(chr(j+96), end = ",")
                print()

        print(subgraph, "connected components")
        if case:
            print()
        case = case - 1

    return 0

main()
