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
    
from collections import deque
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

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        
        tempqueue = deque([])
        qclearcount = 0
        iCurrentPosition = 0
        for num in temperatures:
            while tempqueue:
                minnumber = tempqueue.pop()
                if num > minnumber:
                    temperatures[iCurrentPosition-qdepth] = qdepth
                    qclearcount = qclearcount - 1
                else:
                    tempqueue.appendleft(minnumber)
                    break
            tempqueue.append(num)   
            qclearcount = qclearcount + 1
            iCurrentPosition = iCurrentPosition + 1
        
        while qdepth > 0:
            temperatures[iCurrentPosition-qdepth] = 0
            qdepth = qdepth - 1
        return [temperatures]
    
    def dailyTemperatures3(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices: [i1, i2, ...]

        for i, curr_temp in enumerate(temperatures):
            # While stack is not empty and current temp is warmer than the temp at stack's top index
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
            
        return answer
if __name__ == "__main__":
    c1 = Solution()
    c1.dailyTemperatures3([73,74,75,71,69,72,76,73])
