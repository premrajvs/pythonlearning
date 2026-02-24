class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        target_sum = 0
        prefixsum_index = {}
        prefixsum_set = set()
        i = 0
        for num in nums:
            if num > = target:
                return 1
            target_sum = target_sum + num
            prefixsum_index[target_sum] = i
            prefixsum_set.add(target_sum)
            if prefixsum.get(i)-target 