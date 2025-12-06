def secondLargestElement(nums):
    max = nums[0]
    for i in nums:
        if i > max:
            max = i

    # print(f"Max: {max}")
    while max in nums:
        nums.remove(max)
    # print(nums)

    if len(nums) == 0:
        return -1
    else:
        max2 = nums[0]
        for i in nums:
            if i > max2:
                max2 = i
        # print(f"2nd Max: {max2}")
        return max2
    
# nums = [8, 8, 7, 6, 5]
# nums = [10, 10, 10, 10, 10]
nums = [7, 7, 2, 2, 10, 10, 10]
print(secondLargestElement(nums))
        

                
        