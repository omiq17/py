def main():
    caseNo = 1
    while True:
        edges = int(input())
        if edges == 0:
            break

        e = 0
        c = 1
        graph = {}
        case = {}
        nodeSet = set()
        while True:
            edge = input().split()
            if edge == []:
                break

            for i in range(0, len(edge), 2):
                value1 = int(edge[i])
                value2 = int(edge[i + 1])
                if e < edges:
                    try:
                        graph[value1].append(value2)
                    except(KeyError):
                        graph[value1] = [value2]
                    try:
                        graph[value2].append(value1)
                    except(KeyError):
                        graph[value2] = [value1]
                    e = e + 1
                    nodeSet.add(value1)
                    nodeSet.add(value2)
                else:
                    case[c] = [value1, value2]
                    c  = c + 1


        # print(graph, case)
        # print(len(nodeSet))
        topNode = max(nodeSet)
        totalNode = len(nodeSet)

        def bfs(node, ttl):
            count = 1
            queue = []
            level = [-1] * (topNode + 1)
            queue.append(node)
            level[node] = 0

            while queue!=[]:
                node_u = queue.pop(0)
                try:
                    for i in graph[node_u]:
                        # if visited once, then make sure it won't be repeated
                        if level[i] < 0:
                            count = count + 1
                            level[i] = level[node_u] + 1
                            queue.append(i)
                            if level[i] > ttl:
                                count = count - 1
                                queue.clear()
                                break
                except(KeyError):
                    continue

            return count

        for key, value in case.items():
            if value[0] == 0:
                break
            # print(key)
            nodeVisited = bfs (value[0], value[1])
            notVisited = totalNode - nodeVisited
            print("Case "+ str(caseNo) +": "+ str(notVisited) + " nodes not "\
                "reachable from node "+ str(value[0]) +" with TTL = " \
                + str(value[1]) + ".")
            caseNo = caseNo + 1


main()
#
#
#
#
#
#
#
#
#
