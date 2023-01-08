class Solution:

    def simplifyPath(self, A):
        roots = A.split("/")
        initial = []
        ignoreN = 0
        for root in roots[::-1]:
            if root == "" or root ==".":
                continue
            elif root == "..":
                ignoreN += 1
            elif ignoreN > 0:
                ignoreN -= 1
            else:
                initial.append(root)
        return "/" + "/".join(initial[::-1])

ans = Solution()
A = "/a/./b/../../c/"
print(ans.simplifyPath(A))