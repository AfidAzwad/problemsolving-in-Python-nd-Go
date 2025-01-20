# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
        ''' its built-in method so just study the way of finding this with 2 pointers approach'''

class Solution:

    def firstBadVersion(self, n):
        L, R = 0, n
        while L < R:
            mid = (L + R) // 2
            if isBadVersion(mid):
                R = mid
            else:
                L = mid + 1
        return L

n = 4
solution = Solution()
print(solution.firstBadVersion(n))

"""
Time Complexity: O(log(n))
Space Complexity: O(1)
"""