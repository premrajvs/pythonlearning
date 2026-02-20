from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.numset = {}
        total = 0
        i=0
        for num in nums:
            total = total + num
            self.numset[i]=total
            i=i+1

    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.numset[right] - self.numset[left-1]
        else:
            return self.numset[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)