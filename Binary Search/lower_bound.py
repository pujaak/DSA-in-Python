def findLowerBound(nums, target):
    low = 0
    high = len(nums) - 1
    # lowerBound = len(nums) - 1
    lowerBound = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            lowerBound = mid
            high = mid - 1
        else:
            low = mid + 1
        
    return lowerBound


nums = [1, 2, 4, 5, 7, 8, 9, 10, 13, 17,17, 19, 20]
target = 22
print(findLowerBound(nums, target)) # time complexity : O(log n)