
def binarySearch(nums, target):
    # Init left and right pointers, starting at ends of array
    l = 0
    r = len(nums) - 1

    # Iterate over array, moving pointers as necessary
    while l <= r:
        # The left and right pointers define what part of the array we are currently looking at
        # Middle index is found by doing floor divison (//) of the left and right pointers
        mid = (l + r) // 2
        
        # If number at middle index is target, return middle index
        if nums[mid] == target:
            return mid
        # If target is greater, then move left pointer to current middle index + 1
        # We already checked number at middle value, so we don't care about it anymore
        elif nums[mid] < target:
            l = mid + 1
        # # If target is less than, then move right pointer to current middle index - 1
         # We already checked number at middle value, so we don't care about it anymore
        else:
            r = mid - 1
    # We have checked every number, and found no target. Return some dummy value (in this case -1) to indicate this
    return -1









nums = [2,3,4,10,40]
target = 12

print(binarySearch(nums, target))
# l = 0
# r = len(nums) - 1 # index pointer

# # print(r)

# mid = (l+r) // 2

# print(mid)