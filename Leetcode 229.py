# Description


class Solution:
    def majorityElement(self, nums):
        from collections import Counter
        hash_nums = Counter(nums)
        major_element = []
    
        for j in hash_nums:
            if hash_nums[j] > (len(nums)//3):
                major_element.append(j)
                
        return major_element