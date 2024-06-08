# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Init output array
        ans = []
        
        # Two pointer method since input array is sorted non-descending, start left pointer at beginning of array, and right pointer at end of array
        l = 0
        r = len(nums) - 1
        
        # Loop until pointers intersect
        while l <= r:
            # Compare magnitude of number, since squaring will always result in positive number
            # Whichever is bigger, insert into output array and move respective pointer
            if abs(nums[r]) > abs(nums[l]):
                ans.append(nums[r]**2)
                r -= 1
            else:
                ans.append(nums[l]**2)
                l += 1
        
        # Since we built array backwards, return in reverse order
        return ans[::-1]
        


# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         ans = [num**2 for num in nums]
#         ans.sort()
#         return ans
    
   
nums = [-7,-3,2,3,11]
print(Solution().sortedSquares(nums))