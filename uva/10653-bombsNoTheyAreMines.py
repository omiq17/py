def main():
    while 1:
        # row, col= map(int, input().split())
        try:
            row, col= map(int, input().strip().split())
        except(EOFError):
            break
        if row == 0 and col == 0:
            break

        graph = [[-1 for i in range(col)] for i in range(row)]
        bombRows = int(input().strip())
        for i in range(bombRows):
            bomb = input().strip().split()
            row2 = int(bomb[0])
            for j in range(2, len(bomb)):
                graph[row2][int(bomb[j])] = -2

        srow, scol = map(int, input().strip().split())
        drow, dcol = map(int, input().strip().split())

        queue = [srow, scol]
        graph[srow][scol] = 0

        f = 0
        while queue!=[]:
            node1 = queue[f]
            node2 = queue[f + 1]
            f = f + 2

            moverow = [0, 1]
            movecol = [1, 0]

            for i in range(2):
                nextrow = node1 + moverow[i]
                nextcol = node2 + movecol[i]

                if nextrow <= row-1 and nextcol <= col-1 and \
                    graph[nextrow][nextcol] == -1:
                    graph[nextrow][nextcol] = graph[node1][node2] + 1
                    queue.append(nextrow)
                    queue.append(nextcol)
                    if nextrow == drow and nextcol == dcol:
                        queue.clear()
                        break


        print(graph[drow][dcol])
main()
