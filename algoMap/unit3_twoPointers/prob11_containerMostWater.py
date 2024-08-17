# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Init max_area
        max_area = 0
        
        # Init pointers at end and beginning of array
        i, j = 0, len(height) - 1
        
        # Loop thru array, stopping when pointers meet
        while i < j:
            # Get base and height values
            base = j - i
            # Height is the minimum of the two height values, since the maximum amount of water that will hold will be dependent on smallest height
            current_height = min(height[i], height[j])
            
            # Area of rectangle, and compare to current max area
            area = base * current_height
            max_area = max(max_area, area)
            
            # To maximize area, move the smaller of the two heights
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
    
height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
print(Solution().maxArea(height))