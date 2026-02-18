""" 
twoSum - In this problem, i first used set to check if the requirednumber already exist but then the problem was set only store values. So, I had to come up with another function index of list to get the index value. This is a o(n) itself resulting in o(n2) So the better approach to lookup is always use hashmap
 """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}
        for i, num in enumerate(nums):
            requirednumber = target - nums[i]
            if requirednumber in val_to_index:
               return [i,val_to_index[requirednumber]]
            val_to_index[num] = i