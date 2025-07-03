# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return

            for i in range(1, 4):
                if start + i > len(s): break
                segement = s[start :  start + i]

                if isValidIP(segement):
                    path.append(segement)
                    backtrack(start + i, path)
                    path.pop()
                else:
                    break

        def isValidIP(segement: str):
            if segement[0] == '0':
                return True if len(segement) == 1 else False

            if 0 <= int(segement) <= 255:
                return True

            return False

        backtrack(0, [])
        return res

        
# leetcode submit region end(Prohibit modification and deletion)
