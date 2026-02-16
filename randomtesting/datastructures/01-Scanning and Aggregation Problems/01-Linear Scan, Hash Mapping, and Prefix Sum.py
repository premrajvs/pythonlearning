""" #Common Mistakes

 In Python you use self in a function only when the function is declared inside a class because self makes it a instance method.
 if outside a class, it is just another variable.

 Second mistake with function, if a function is inside a class, it is mandatory to have a variable called self as first arg.

 When you want to call a class, you do not need new operator. In python calling a class is same as calling a function.
 Second, when you just say fi=findminmax, you are not creating a new object. you are renaming the class findminmax. like changing the name of the blueprint. Instead you should use () next to class name. now it creates object

 In Java you can have multiple classes and functions and then declare void main function in on class and it automatically becomes the entry point. But python runs top down. So, it does not work that way. When you import the python class in another class in a big project, you dont have to worry about what gets called when because code logic takes care of that. But if you want to run a file directly, use __name__ == "__main__". Python knows to run this automatically.
 
 In python if i want to search if something exist, fastest data structure is Hashmap but if you do not want values, faster is set because it does not store any values.
 """

""" 
It is very important to understand how Stack and Queue works so you can use it in different scenarios. For example, in min stack requirement I am using stack. 

Understanding summary.

List [1, 2, 3] = List in Python always follows stack

Step	Action	List State [Head ... Tail]	Head Value	Tail Value
1	Push 1	[1]	1	1
2	Push 2	[1, 2]	1	2
3	Push 3	[1, 2, 3]	1	3
4	Push 4	[1, 2, 3, 4]	1	4
5	Push 5	[1, 2, 3, 4, 5]	1	5

Always first element is Head = 1
Always last element is Tail = 3
Always push and pop both interacts with Tail that is 3
Always when i append, it moves Tail to new element

Now For Queue - default data structure is collections dequeue
Step	Action	Deque State [Head ... Tail]	Head	Tail
1	Enqueue 1	[1]	1	1
2	Enqueue 2	[1, 2]	1	2
3	Enqueue 3	[1, 2, 3]	1	3
4	Enqueue 4	[1, 2, 3, 4]	1	4
5	Enqueue 5	[1, 2, 3, 4, 5]	1	5

Always first element is Head = 1
Always last element is Tail = 3
**DIFFERENCE ** Push interacts with Tail and Pop interacts with Head
.pop() is to remove the tail element and see the tail element
.appendleft(value) is to add an element to head
Always when i append, it moves Tail to new element

When you want to rotate an array, always use % operator target%length so it becomes faster. If an array has 5 elements and if you want to rotate 5 times. 5%5=0 - no rotation needed. if rotation target is 6, 6%5=1 so you just rotate once. it is same effect.
 """
from collections import deque
from typing import List


class findminmax:
    def checkalllinearly(self,arrayofnumber):
        if not isinstance(arrayofnumber,(list)):
            return TypeError
        if len(arrayofnumber)<1:
            return None,None
        minimum = arrayofnumber[0]
        maximum = arrayofnumber[0]
        for number in arrayofnumber:
            if minimum>number:
                minimum=number
            if maximum<number:
                maximum=number
        return minimum,maximum

class callingclass:
    def method1(self):
        #do nothing
        print()

    def main(self,args):
        fi = findminmax()
        #data=[]
        data = [1,3,5,2,4,6]
        print(fi.checkalllinearly(data))

class Solution:
    def maxProfit_DoubleLoop(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        profit = 0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] - prices[i]>profit and prices[j]>prices[i]:
                    profit = prices[j] - prices[i]
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        profit = 0
        minimumprice = prices[0]
        maxprofit = 0
        for i in range(0,len(prices)):

            if prices[i]<minimumprice:
                minimumprice = prices[i]
            elif prices[i] - minimumprice > maxprofit:
                maxprofit = prices[i] - minimumprice
        return maxprofit
    
    def containsDuplicate_slow(self, nums: List[int]) -> bool:
        if len(nums)<1:
            return False
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==0:
                return True
        return False
    
    def containsDuplicate_fast(self, nums: List[int]) -> bool:
        if len(nums)<1:
            return False
        #nums = sorted(nums)
        mymap = {}
        for i in range(0,len(nums)):
            if nums[i] in mymap:
                return True
            else:
                mymap[nums[i]] = 0
        return False
    
    def containsDuplicate_fastest(self, nums: List[int]) -> bool:
        if len(nums)<1:
            return False
        #nums = sorted(nums)
        mymap = set()
        for i in range(0,len(nums)):
            if nums[i] in mymap:
                return True
            mymap.add(nums[i])
        return False

    def majorityElement_slow(self, nums: List[int]) -> int:
        targetcount = len(nums)/2
        mymap = {}
        for i in range(0,len(nums)):
            if nums[i] in mymap:
                mymap[nums[i]] = mymap[nums[i]]+1
            else:
                mymap[nums[i]] = 1
            if mymap[nums[i]] >= targetcount:
                    return nums[i]

    def pivotIndex(self, nums: List[int]) -> int:
        lengthofnums = len(nums)
        totalsum = sum(nums[0:lengthofnums])
        leftsum = 0
        for i in range(0,lengthofnums): 
            if totalsum-leftsum-nums[i] == leftsum:
                return i
            leftsum = leftsum + nums[i]
        return -1
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consequtiveones = 0
        maxcon = 0
        totallength = len(nums)
        for i in range(totallength):
            if nums[i] == 1:
                consequtiveones = consequtiveones+1
                if maxcon < consequtiveones:
                    maxcon = consequtiveones
            elif (nums[i] == 0 or i+1 == totallength) and consequtiveones > 0:
                consequtiveones = 0
                #if maxcon < consequtiveones:
                   # maxcon = consequtiveones
        return maxcon
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsqueue = deque(nums)
        n = len(nums)
        k %= n 
        while k>0:
            lastnumber = numsqueue.pop()
            numsqueue.appendleft(lastnumber)
            k=k-1 
        nums[:] = list(numsqueue)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val <= current min, push to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the value being removed is the current minimum, pop from min_stack too
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

if __name__ == "__main__":
    c1 = callingclass()
    c1.main(None)
    s1 = Solution()
    s1.maxprofile()
