class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        queue = []
        visited = set()
        repeated = set()
        res = []
        for ele in A:
            if ele not in visited:
                queue.append(ele)
                visited.add(ele)
            elif ele not in repeated:
                repeated.add(ele)
                queue.remove(ele)
            letter = queue[0] if len(queue) > 0 else '#'
            res.append(letter)
        return ''.join(res)

ans = Solution()
A = "abadbc"
print(ans.solve(A))