def recursiveBinarySearch(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursiveBinarySearch(arr, low, mid - 1, target)
    else:
        return recursiveBinarySearch(arr, mid + 1, high, target)

nums = [3, 6, 7, 8, 10, 14, 15, 17, 19] # 3
target = 8
print(recursiveBinarySearch(nums, 0, len(nums) - 1, target ))