# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.



class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        ans = []
        
        nums.sort()
        n = len(nums)
        i = 0
        
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue    
 
            target = -nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                summ = nums[j] + nums[k]
                if summ == target:
                    ans.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                    
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                        
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                    
                elif summ > target:
                    k -= 1
                elif summ < target:
                    j += 1
        
        return ans
    
# nums = [-1,0,1,2,-1,-4]
nums = [0, 0, 0]
# nums = [-2,0,0,2,2]
print(Solution().threeSum(nums))