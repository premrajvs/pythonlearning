class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftpos = 0
        rightpos = len(height)-1
        maxwater = 0
        while leftpos < rightpos:
            capacity = (rightpos - leftpos)* min(height[leftpos],height[rightpos])
            if capacity > maxwater:
                maxwater = capacity
            if height[leftpos] < height[rightpos]:
                leftpos = leftpos+1
            else:
                rightpos = rightpos -1
        return maxwater