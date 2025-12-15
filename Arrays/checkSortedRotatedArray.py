# time complexity: O(N)
def checkSortedRotated(nums):
    count = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            if nums[len(nums) - 1] <= nums[0] and count == 0:
                count = count+1
                continue
            return False
    print(count)
    return True

# [1,1,1] [6,10,6] [7,9,1,1,1,3]
# nums = [3,4,5,1,2] # True - rotated
# nums = [2,1,3,4] # false
# nums = [1, 1, 1]
# nums = [6, 10, 6]
# nums = [7,9,1,1,1,3]
nums = [2,7,4,1,2,6,2]
print(checkSortedRotated(nums))