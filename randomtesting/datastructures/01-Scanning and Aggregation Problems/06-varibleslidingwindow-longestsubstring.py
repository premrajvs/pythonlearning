class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keyword is Substring. So, it is a window problem
        left = 0
        right = 0
        maxlen = right-left
        mymap = {}
        for c in s:
            #print(mymap)
            right = right+1
            if c in mymap:
                if mymap.get(c) + 1 > left:
                    left = mymap.get(c) + 1
                #print("new left",left)
                #print("right",right)
                mymap[c] = right-1
            else:
                #print("else left",left)
                #print("else right",right)
                mymap[c] =  right-1
            if right - left > maxlen:
                    maxlen = right - left
            #print("maxlen",maxlen)
        #if left == 0:
        #    return maxlen
        #elif left > 0:
        return maxlen