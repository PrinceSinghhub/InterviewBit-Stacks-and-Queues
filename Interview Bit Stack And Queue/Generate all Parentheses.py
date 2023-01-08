class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        d = {"(": ")", "[": "]", "{": "}"}
        l = []
        if (len(A) == 1) or (A[0] not in d):
            return 0
        for i in A:

            if i in d:
                l.append(i)

            elif len(l) == 0:
                return 0
            else:
                if i == d[l[-1]]:
                    l.pop()

                else:
                    return 0
        if len(l) == 0:
            return 1
        else:
            return 0

ans = Solution()
a = "{{(())}}"
print(ans.isValid(a))




