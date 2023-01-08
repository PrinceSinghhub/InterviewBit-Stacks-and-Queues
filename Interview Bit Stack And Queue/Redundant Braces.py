class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):

        stack = []
        flag = False

        for i in A:

            if i == '(':

                stack.append(i)
                flag = False

            elif i == ')':
                temp = stack.pop()

                if temp == '(':
                    return 1

                stack.pop()
                flag = False

            elif i in ('+', '*', '-', '/') and flag == False:
                stack.append('x')
                flag = True

        return 0

ans = Solution()
A = "((a+b))"
print(ans.braces(A))