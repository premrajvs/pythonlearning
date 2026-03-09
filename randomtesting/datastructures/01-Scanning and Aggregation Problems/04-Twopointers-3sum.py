class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        mylist = []
        nums.sort()
        #left = 1
        #right = len(nums)-1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    mylist.append([nums[left],nums[i],nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and nums[left-1] == nums[left]:
                            left = left + 1
                    while left < right and nums[right+1] == nums[right]:
                            right = right - 1
                if nums[left] + nums[right] + nums[i] < 0:
                    left = left + 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right = right - 1
        return mylist
                