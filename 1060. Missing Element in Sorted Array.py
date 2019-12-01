# Given a sorted array A of unique numbers, 
# find the K-th missing number starting from the leftmost number of the array.

# example 1:
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5

# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.

# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.



class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_missed = 0 #record total number of missed numbers
        pre = 0 # record total number of last round missing number
        
        for i in range(1,len(nums)):  
            if nums[i] - nums[i-1] > 1:  # if missing element exist
                pre = total_missed   # record previous round 
                total_missed += nums[i] - nums[i-1] - 1  # update total to itself plus current # - the number before - 1
                # minus 1 because to exclude the current. Ex: 4,7  7-4 = 3 but only 2 numbers are missing.

                # if k meets, then return the number before + (k - last iteration)        
                # [4,7,9,8]
                # [4,5,6,7]
                # difference = [0,2,3,3]                           
                if total_missed >= k:
                    return nums[i-1] + (k - pre)
                
                # if not then return the last digit + k - total
        return num[-1] + (k - total_missed)