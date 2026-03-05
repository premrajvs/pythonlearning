class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        keylist = {}
        numlength = len(numbers)
        index2 = len(numbers)-1
        index1 = 0
        n = target
        for i in range(0,numlength):
            #if numbers[i] <= n:
            #    print("condition true")
            index2 = i
            n = n - numbers[i]
            if n in keylist:
                index1 = keylist.get(n)
                return [index1+1,index2+1]
            n = target
            keylist[numbers[i]] = i
                