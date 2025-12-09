# def secondLargestElement(nums):
#     print(f"1st menthod, len of nums: {len(nums)}")
#     max = nums[0]
#     for i in nums:
#         if i > max:
#             max = i

#     # print(f"Max: {max}")
#     while max in nums:
#         nums.remove(max) # this modifies the original list
#     # print(nums)

#     if len(nums) == 0:
#         return -1
#     else:
#         max2 = nums[0]
#         for i in nums:
#             if i > max2:
#                 max2 = i
#         # print(f"2nd Max: {max2}")
#         return max2
    


# second way
def secondLargestElement2(nums):
    largest = slargest = -1
    
    for i in range(0, len(nums)):
        if nums[i] > largest : 
            largest = nums[i]
            
    for i in range(0,len(nums)):
        if nums[i] > slargest and nums[i] != largest:
            slargest = nums[i]
    return slargest


nums = [8, 8, 7, 6, 5]
# nums = [10, 10, 10, 10, 10]
# nums = [7, 7, 2, 2, 10, 10, 10]
# nums = [1, 2, 3, 1, 2, 1]
# print(secondLargestElement(nums))
print(secondLargestElement2(nums))