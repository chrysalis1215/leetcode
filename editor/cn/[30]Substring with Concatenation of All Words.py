# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict, Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_dict = defaultdict(int)

        word_size = len(words[0])
        flatten_words = "".join(words)
        window_size = len(flatten_words)
        words_cnt =  Counter(flatten_words)
        for word in words:
            word_dict[word] += 1

        if window_size > len(s):
            return []

        left = 0
        right = 0
        res = []
        while right < len(s):

            if s[right] not in words_cnt:
                right += 1
                left = right
            elif right - left + 1 == window_size:
                temp = defaultdict(int)
                for i in range(left, right + 1, word_size):
                    min_window = s[i:i+word_size]
                    if min_window in word_dict:
                        temp[min_window] += 1
                    else:
                        left += 1
                        right += 1
                        break
                else:
                    if temp == word_dict:
                        res.append(left)
                    left += 1
                    right += 1
            else:
                right += 1


        return res



        
# leetcode submit region end(Prohibit modification and deletion)
res = Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", 'aa'])
print('res', res)