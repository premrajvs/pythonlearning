class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0
        prefixsum_map =  {0:1}
        for num in nums:
            current_sum = current_sum + num
            if current_sum-k in prefixsum_map:              
                count = count + prefixsum_map.get(current_sum-k)
            prefixsum_map[current_sum] = prefixsum_map.get(current_sum,0) + 1
        return count