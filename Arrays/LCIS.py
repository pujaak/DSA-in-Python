class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        count = 1
        lcis = 1
        for i in range(1,len(nums)):
            
            if nums[i] > nums[i-1] :
                count += 1
            else:
                count = 1
            if count > lcis:
                lcis = count
            print(i, nums[i], count, lcis)
        return lcis


sol = Solution()
# nums = [1,3,5,4,7] # 3
# nums = [2,2,2,2,2] # 1
nums = [1,3,5,7] # 4
print(sol.findLengthOfLCIS(nums))