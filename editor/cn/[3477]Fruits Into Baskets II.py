# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        usedSet = set(range(0, len(baskets)))

        for f in fruits:
            for index in usedSet:
                if f <= baskets[index]:
                    usedSet.remove(index)
                    break

        return len(usedSet)


        
# leetcode submit region end(Prohibit modification and deletion)
