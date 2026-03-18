""" Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0] """

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        tempstack = []
        ipos = 0
        posmap = {}
        valmap = {}
        for num in temperatures:
            posmap[num] = ipos
            valmap[num] = 0
            while tempstack:
                temp = tempstack.pop()
                if num > temp:
                    valmap[temp] = posmap[num]-posmap[temp]
                else:
                    tempstack.append(temp)
                    break
            tempstack.append(num)   
            ipos = ipos + 1
        
        return [valmap[num] for num in temperatures]

if __name__ == "__main__":
    c1 = Solution()
    c1.dailyTemperatures([73,74,75,71,69,72,76,73])
