from jovian.pythondsa import evaluate_test_cases

class binarysearch:
    testcaselist = []
    def __init__(self):
        pass

    def addtestcases(self,test):
        self.testcaselist.append(test)
    
    def createtestcase(self):
        test1 = {
            'input': {
                'inputarray': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                'searchvalue': 5
            },
            'output': 4
        }
        self.addtestcases(test1)
        test2 = {
            'input': {
                'inputarray': [1, 5, 2, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                'searchvalue': 11
            },
            'output': -1
        }
        self.addtestcases(test2)

        test = {
            'input': {
                'inputarray': [],
                'searchvalue': 11
            },
            'output': -1
        }
        self.addtestcases(test)

        test = {
            'input': {
                'inputarray': [9,9,9,9,9,9,9,9,9,9],
                'searchvalue': 9
            },
            'output': 0
        }
        self.addtestcases(test)
        
        test = {
            'input': {
                'inputarray': [9999999999,0,1111111,2222222,3333333,4444444,5555555,6666666,7777777,8888888,9999999],
                'searchvalue': 1111111
            },
            'output': 2
        }
        self.addtestcases(test)

    def performLinearsearch(self, inputarray, searchvalue):
        iCurrentPosition = 0
        tail = len(inputarray) - 1
        # Step 1 : If the array is empty, return -1. So, i am checking if head is equal to tail
        if iCurrentPosition >= tail:
            return -1
        else:
            for i in range(len(inputarray)):
                if inputarray[i] == searchvalue:
                    return i
            return -1

    def performBinarysearch(self, inputarray, searchvalue):
        iCurrentPosition = 0
        tail = len(inputarray) - 1
        # Step 1 : If the array is empty, return -1. So, i am checking if head is equal to tail
        if iCurrentPosition >= tail:
            return -1
        else:
            inputarray.sort()  # Ensure the array is sorted for binary search
            iCurrentPosition = len(inputarray)//2
            if inputarray[iCurrentPosition] == searchvalue:
                return iCurrentPosition
            elif inputarray[iCurrentPosition] < searchvalue:    
                return self.performBinarysearch(inputarray[iCurrentPosition+1:], searchvalue) 
            return -1
    
if __name__ == "__main__":
    bs = binarysearch()
    bs.createtestcase()
    print(bs.testcaselist)
    #for test in bs.testcaselist:
     #   print(f"Input Array: {test['input']['inputarray']}, Search Value: {test['input']['searchvalue']}, Expected Output: {test['output']}")
        #print(bs.performLinearsearch(test['input']['inputarray'], test['input']['searchvalue']) == test['output'])
    
    evaluate_test_cases(bs.performLinearsearch,bs.testcaselist)
    
    