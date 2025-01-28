class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        # Make map to remember where we have seen numbers as we iterate
        hashmap = {} # {num: index}

        for i in range(len(nums)):
            current = nums[i]
            # current + x = target
            # x = target - current
            x = target - current

            if x in hashmap:
                return [hashmap[x], i]

            hashmap[current] = i

        return []

s = Solution()
print(s.twoSum([2,15,11,7], 9))