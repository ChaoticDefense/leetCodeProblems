# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1



# class Solution:
#     def search(self, nums: list[int], target: int) -> int:

#         # First finding pivot point from binary search
#         l = 0
#         r = len(nums) - 1
#         p = -1

#         while l <= r:
#             m = (l + r) // 2
#             if nums[m] > nums[m + 1]:
#                 # Found pivot point
#                 p = m
#                 break
#             elif nums[l] > nums[m]:
#                 r = m - 1
#             elif nums[m] > nums[r]:
#                 l = m + 1

#         if l == r:
#             p = l

#         if target >= nums[0] and target <= nums[p]:
#             l = 0
#             r = p
#         else:
#             l = p
#             r = len(nums) - 1

#         while l <= r:
#             m = (l + r) // 2
#             if nums[m] == target:
#                 return m
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 r = m - 1

#         return -1




class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # Left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m]
            else:



            # elif target < nums[m]:
            #     if target < nums[l]:
            #         l = m + 1
            #     else:
            #         r = m - 1
            # elif target > nums[m]:
            #     if target > nums[r]:
            #         r = m -1
            #     else:
            #         l = m + 1
            
        return -1
        
    

nums = [4,5,6,7,0,1,2]
target = 0

print(Solution().search(nums, target))