from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        size = len(nums)
        for i in range(size - 2):

            # 跳过宠物
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = size - 1

            target = 0 - nums[i]

            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum > target:
                    right -= 1
                else:
                    left += 1

        return res

        
# leetcode submit region end(Prohibit modification and deletion)

Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])