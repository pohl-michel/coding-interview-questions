from typing import List

# Naive solution O(n²)
# where we iterate with double pointers

# with hashmap
# time complexity O(n)
# space complexity O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pos = {}
        for i, elt in enumerate(nums):
            
            complementary = target - elt
            if complementary in pos:
                return pos[complementary], i
            
            if elt not in pos:
                pos[elt] = i


# in case the array is sorted, we can use two pointers:
# time complexity O(n)
# space complexity O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        l, r = 0, n-1
        
        my_sum = nums[l] + nums[r]
        
        while my_sum != target:
            if my_sum > target:
                r -= 1
            elif my_sum < target:
                l += 1
            my_sum = nums[l] + nums[r]
        
        return l, r