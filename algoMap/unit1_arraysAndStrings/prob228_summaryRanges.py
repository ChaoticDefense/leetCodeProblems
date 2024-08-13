# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

#     "a->b" if a != b
#     "a" if a == b

 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # Edge case when nums is empty
        if len(nums) == 0:
            return []
        
        # Init output
        out = []
        
        # Starting and ending indices of nums
        A = len(nums) - 1
        i = 0
        
        # Separate pointer for starting point of check interval
        begin = 0
        
        # Iterate over array
        while i < A:
            # Check for gaps between numbers
            if nums[i+1] - nums[i] > 1:
                # If starting point is same as current pos, append only num
                if begin == i:
                    out.append(str(nums[i]))
                # Output range of nums
                else:
                    out.append(str(nums[begin])+"->"+str(nums[i]))
                
                # If gap was found, move starting point to next num after i
                begin = i + 1
            # No matter what, move i
            i += 1
        
        # We reached end of array, do same checks as above
        if begin == i:
            out.append(str(nums[i]))
        else:
            out.append(str(nums[begin])+"->"+str(nums[i])) 

        return out

# nums = [0,1,2,4,5,7]
nums = [0,2,3,4,6,8,9]
print(Solution().summaryRanges(nums))