class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_dict = {}
        for num in nums:
            if top_dict.get(num):
                top_dict[num] = top_dict[num] + 1
            else:
                top_dict[num] = 1
        
        sorted_list = sorted(top_dict.items(), key=lambda x: x[1], reverse=True)

        return list(map(lambda x: x[0], sorted_list))[0:k:1]

        