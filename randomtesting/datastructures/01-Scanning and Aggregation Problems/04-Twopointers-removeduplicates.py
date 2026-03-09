class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myset = set()
        k = 0
        target = 0
        for i in range(len(nums)):
            if nums[i] not in myset:
               myset.add(nums[i])
               nums[target] = nums[i]
               target = target + 1
               k=k+1
        for j in range(target,len(nums)):
            nums[j] = "_"
        return k