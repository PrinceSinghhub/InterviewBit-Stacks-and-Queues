class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def nearestHotel(self, A, B):
        n = len(A)
        m = len(A[0])

        from collections import deque
        dist = [[-1 for j in range(m)] for i in range(n)]
        qi = deque()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    dist[i][j] = 0
                    qi.append((i, j))

        while qi:
            x, y = qi.popleft()
            d = dist[x][y]
            if x + 1 < n:
                if dist[x + 1][y] == -1:
                    dist[x + 1][y] = d + 1
                    qi.append((x + 1, y))
            if x - 1 >= 0:
                if dist[x - 1][y] == -1:
                    dist[x - 1][y] = d + 1
                    qi.append((x - 1, y))
            if y + 1 < m:
                if dist[x][y + 1] == -1:
                    dist[x][y + 1] = d + 1
                    qi.append((x, y + 1))
            if y - 1 >= 0:
                if dist[x][y - 1] == -1:
                    dist[x][y - 1] = d + 1
                    qi.append((x, y - 1))

        result = []
        for query in B:
            x, y = query
            result.append(dist[x - 1][y - 1])

        return result