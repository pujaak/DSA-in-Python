class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pos_arr = []
        # pos_arr2 = []
        # pos_arr3 = []
        # count = 0
        # pos_arr3.append(count)
        pos_arr.append(nums[0])
        # pos_arr2.append(0)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pos_arr.append(nums[i]) # it contains the unique elements
                # pos_arr2.append(i) # it contains the position of first occurence of unique elements
                # count += 1
                # pos_arr3.append(count) # it just contsin 0 to len unique elments count

       

        # print(len(pos_arr), pos_arr)
        # print(len(pos_arr2), pos_arr2)
        # print(len(pos_arr3), pos_arr3)
        # print(count)
        # print("sdfhke")
        for i in range(len(pos_arr)):
            # print(i, pos_arr[i])
            nums.insert(i, pos_arr[i])

        return len(pos_arr)
      
sol = Solution()
# nums = [1,1,2] # 2, nums = [1,2,_]
# nums = [0,0,1,1,1,2,2,3,3,4] # 5, nums = [0,1,2,3,4,_,_,_,_,_]
nums = [3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 8, 8] # 6, nums = [3, 4, 5, 6, 7, 8,_,_,_,_,_,_]
print(sol.removeDuplicates(nums))
print(nums)
# i need to make changes in existing array
































# try aoviding talking to the left her. and no sharing anything or showing to people esp my cursl stuff, and ik even rj and mg is same so yeah at a distance is fien.
# yk what if best friends means insensitve laugh , then i sont want to have one. fuck internet advice. lets just be good frineds that's it.
# did she say mareng n apko ? i wonde r and is he now wants her idk. 
# see dicussing her could only waste my tie and my energy and yeahmujhe kya lena dena jo kre ye . avoid the gossip so i dont wanna know what is going in her life . bhar m jaye
# yup that's right what else has she dobe. and i have if ever me dragged cuz of such peopl , yk see ksi, and also sometime ar , fuck all toegther eeat and sleep shit. i wanna do it i will do it if you wont. 
# also i like the silence and i so much not wana talk to any . and continue no  need to excited even for any 
