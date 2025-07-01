# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start+1, len(s) + 1):
                part = s[start:end]

                if isPalindrome(part):
                    path.append(part)
                    backtrack(end, path)
                    path.pop()




        def isPalindrome(s) -> bool:
            left = 0
            right = len(s)

            while left < right:
                if s[left] == s[right - 1]:
                    left += 1
                    right -= 1
                else:
                    return False

            return True

        backtrack(0,[])
        return  res

# leetcode submit region end(Prohibit modification and deletion)

a = Solution().partition('aab')
print(a)