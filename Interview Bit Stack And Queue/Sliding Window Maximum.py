from collections import deque


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        d = deque(A[:B])
        sm, n = [max(d)], len(A)
        for i in range(B, n):
            temp = d.popleft()
            d.append(A[i])
            if A[i] > sm[-1]:
                sm.append(A[i])
            elif temp < sm[-1]:
                sm.append(sm[-1])
            else:
                sm.append(max(d))
        return sm


# bruteforce Approch
class Solution1:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):

        if B > len(A):
            return 1

        ans = []

        for i in range(len(A) - B + 1):
            temp = A[i:B + i]
            print(temp)
            ans.append(max(temp))
        return ans

ans = Solution()
arr = [9,4,2,7,3,5,8,1]
b= 4
print(ans.slidingMaximum(arr,b))