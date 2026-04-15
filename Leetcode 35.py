# Solution should run on log n complexity

class Solution:
    def searchInsert(self, nums, target) -> int:
        low = 0
        high = len(nums)-1
        position = -1
        
        while low <= high:
            mid = (high+low)//2

            if target == nums[mid]:
                position = mid
                break
            elif target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        
        if position != -1:
            return position
        else:
            insert_position = -1
            
            if target > min(nums) and len(nums) >= 1:
                for i in nums:
                    if i < target:
                        insert_position = nums.index(i)+1
            
                nums.insert(insert_position, target)
                return nums.index(target)

            elif target < min(nums):
                nums.insert(nums.index(min(nums)), target)
                return nums.index(target)
            
            else:
                return 0