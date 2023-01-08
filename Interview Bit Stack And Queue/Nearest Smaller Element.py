# optimize code
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        """
        Find nearest element which is less than the
        current element and on its left.
        """
        gL = [-1]
        smaller = [A[0]]
        for i in A[1:]:
            notAppended = True
            j = len(smaller) - 1
            while j >= 0:
                if i > smaller[j]:
                    gL.append(smaller[j])
                    smaller.append(i)
                    notAppended = False
                    break
                else:
                    smaller.pop()
                    j -= 1
            if notAppended:
                gL.append(-1)
                smaller.append(i)
        return gL
class Solution1:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):

        ans = []

        ans.append(-1)

        for i in range(1, len(A)):

            # print(A[i])

            temp = A[0:i]

            # print(temp)




            if min(temp) < A[i]:
                for j in temp[::-1]:
                    if j < A[i]:
                        ans.append(j)
                        break

            else:
                ans.append(-1)



        return ans


ans = Solution()
A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
print(ans.prevSmaller(A))