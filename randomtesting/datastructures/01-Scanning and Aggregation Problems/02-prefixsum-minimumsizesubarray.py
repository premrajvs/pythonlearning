class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        target_sum = 0
        # Initialize with a number larger than any possible array length
        min_len = len(nums) + 1 
        initial = 0
        
        for current in range(len(nums)):
            # 1. Add the current number to our running total
            target_sum += nums[current]
            
            # 2. While the sum is enough, try to make the window smaller
            # We use a 'while' loop instead of an 'if' to shrink as much as possible
            while target_sum >= target:
                # Update the smallest length we've seen so far
                min_len = min(min_len, current - initial + 1)
                
                # Subtract the leftmost number and move the 'initial' pointer forward
                target_sum -= nums[initial]
                initial += 1
        
        # 3. If min_len was never updated, it means no subarray was found
        return min_len if min_len <= len(nums) else 0
