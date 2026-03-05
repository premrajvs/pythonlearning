class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        imv = 0
        for i in range(len(nums)-1,-1,-1):
           #print("imv",imv)
           # print("num",nums[i])
            if nums[i] != 0:
                imv = imv + 1
            else:
                if imv>0:
                    ci = i
                    cimv = imv
                    #print("nums before",nums)
                    while cimv > 0:
                        #print("cimb",cimv)
                        #print("nums",nums)
                        nums[ci] = nums[ci+1]
                        cimv = cimv -1
                        ci = ci + 1
                    nums[i+imv] = 0
                    #print("nums after",nums)