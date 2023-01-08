class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        stack = []
        result = 0
        i = 0
        while i < len(A):
            if not stack or A[stack[-1]] <= A[i]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                tmp = A[tp] * (i - stack[-1] - 1 if stack else i)
                if result < tmp:
                    result = tmp

        while stack:
            tp = stack.pop()
            tmp = A[tp] * (i - stack[-1] - 1 if stack else i)
            if result < tmp:
                result = tmp

        return result

ans = Solution()
A = [2, 1, 5, 6, 2, 3]
print(ans.largestRectangleArea(A))