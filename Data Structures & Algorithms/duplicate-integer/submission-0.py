class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = {}
        for num in nums:
            exist[num] = exist.get(num, 0) + 1
            if exist[num] > 1:
                return True

        return False
        