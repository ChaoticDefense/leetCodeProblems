# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).



# import statistics


# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
#         nums = nums1 + nums2
#         nums.sort()
        
#         return statistics.median(nums)

# Solution made by ChatGPT using binary search
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize the number of comparisons
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        
        low, high = 0, x
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
        
        raise ValueError("Input arrays are not sorted.")

    
print(Solution().findMedianSortedArrays([1,3], [2]))