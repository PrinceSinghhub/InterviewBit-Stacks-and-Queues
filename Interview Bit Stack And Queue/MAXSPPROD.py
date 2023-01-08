class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        if len(A)<3:
            return 0
        stack = []
        max_prod = 0
        for i in range(len(A)-1, -1, -1):
            while stack and A[i] > A[stack[-1]]:
                stack.pop()
                if stack:
                    max_prod = max(max_prod, i*stack[-1])
            stack.append(i)
            if max_prod > 0 and stack[-1] <= len(A)/2:
                break
        return max_prod%1000000007

ans = Solution()
A = [1, 4, 3, 4]
print(ans.maxSpecialProduct(A))