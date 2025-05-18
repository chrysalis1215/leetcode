from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        mx = max(arr)
        size = len(arr)

        s = [0] * (mx + 2)

        ans = 0

        for j, _ in enumerate(arr):
            for k in range(j + 1, size):
                if (abs(arr[j] - arr[k]) > b):
                    continue
                l = max(arr[j] - a, arr[k] - c, 0)
                r = min(arr[j] + a, arr[k] + c, mx)
                # arr[i] 的约束条件为 l <= arr[i] <= r && i < j
                if l > r:
                    continue
                ans += s[r + 1] - s[l]

            # 维系一个前缀和数组，跟传统的前缀和数组不同的是，s[k]表示 range 区间
            # 若arr[j] = 10, 则arr的值在 10 - 1001 区间中，大于10的值均加一
            for k in range(arr[j] + 1, (mx + 2)):
                s[k] += 1

        return ans

# leetcode submit region end(Prohibit modification and deletion)
