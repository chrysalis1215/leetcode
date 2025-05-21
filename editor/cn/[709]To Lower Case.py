# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for i in s:
            res += chr(ord(i) | 32) if  'A' <= i <='Z' else i
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
