class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        stack = []

        for i in A:
            if i == '(':
                stack.append(i)

            if i == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return 0

        if len(stack) == 0:
            return 1

        return 0

ans = Solution()
A = "(()())"
print(ans.solve(A))