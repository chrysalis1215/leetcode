# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        res = pow(10, 5) + 1
        if size == 3:
            return sum(nums)

        nums.sort()

        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = size - 1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if temp == target:
                    return temp
                elif temp > target:
                    right -= 1
                else:
                    left += 1

                res = temp if abs(temp - target) < abs(res - target) else res

                # 需要寻找相近值，不是唯一值，无需跳过重复值
                # while left < right and nums[left] == nums[left - 1]:
                #     left += 1
                # while left < right and right + 1 < size and nums[right] == nums[right + 1]:
                #     right -= 1

        return res
# leetcode submit region end(Prohibit modification and deletion)

