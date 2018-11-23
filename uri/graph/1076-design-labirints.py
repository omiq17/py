def main():
    case = int(input())

    while case:
        a = input()
        nodes, edges = map(int, input().split())
        graph = dict( [(k,[]) for k in range(nodes)] )
        
        for i in range(edges):
            edge1, edge2 = map(int, input().split())
            graph[edge1].append(edge2)
            graph[edge2].append(edge1)

        total = 0
        for i in graph:
            graph[i] = list(set(graph[i]))
            total += len(graph[i])

        # print(graph)
        print(total)
        case = case - 1

main()
