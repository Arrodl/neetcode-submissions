class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = 1

        result = []

        while left_index < len(nums) - 1:
            res = nums[left_index] + nums[right_index]
            if res == target:
                result = [left_index, right_index]
                return result
            elif right_index < len(nums) - 1:
                right_index += 1
            else:
                left_index += 1
                right_index = left_index + 1        

        return result