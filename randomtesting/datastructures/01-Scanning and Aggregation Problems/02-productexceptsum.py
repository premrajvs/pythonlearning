class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_hashmap = {0:1}
        nlen = len(nums)
        right_hashmap = {nlen-1:1}
        target = [1]*nlen
        j = nlen-2
        for i in range(1,nlen):
            left_hashmap[i] = left_hashmap.get(i-1)*nums[i-1]
            right_hashmap[j] = right_hashmap.get(j+1) * nums[j+1]
            j = j-1
        for i in range(0,nlen):
            target[i] = left_hashmap[i] * right_hashmap[i]
            i=i+1
        return target