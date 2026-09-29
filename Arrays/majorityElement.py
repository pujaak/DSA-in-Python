class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hmap = dict()
        print(len(nums))
        print(len(nums) // 2)
        print(len(nums) / 2)
        for i in range(0, len(nums)):
            if nums[i] in hmap.keys():
                hmap[nums[i]] += 1
            else: 
                hmap[nums[i]] = 1
        for key in hmap.keys():
            if hmap[key] >= len(nums) / 2:
                return key
        
sol = Solution()
# nums = [1, 2, 1]
# nums = [2,2,1,1,1,2,2]
nums = [6, 5, 5]
print(sol.majorityElement(nums))