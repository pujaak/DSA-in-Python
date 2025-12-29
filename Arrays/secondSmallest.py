def secondSmallestElement(nums):
    smallest = ssmallest = float('inf')
    for i in range(0, len(nums)):
        if nums[i] < smallest:
            ssmallest = smallest
            smallest = nums[i]
        elif nums[i] > smallest and nums[i] < ssmallest:
            ssmallest = nums[i]
    return ssmallest
    


# nums = [8, 8, 7, 6, 5]
# nums = [10, 10, 10, 10, 10]
# nums = [7, 7, 2, 2, 10, 10, 10]
nums = [1, 2, 3, 1, 2, 1]
print(secondSmallestElement(nums))