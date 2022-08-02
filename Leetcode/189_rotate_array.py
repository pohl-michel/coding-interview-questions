from typing import List
# https://stackoverflow.com/questions/57505071/nameerror-name-list-is-not-defined



# time complexity O(n)
# memory complexity O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        temp = nums.copy()

        for i in range(n):
            nums[i] = temp[i - k % n]



# Similar solution with array slicing

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        temp = nums[-k:]
        del nums[-k:]
        nums[:0] = temp



# Similar solution:

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k:] + nums[:-k]


# Solution with array reversal
# time complexity O(n)
# memory complexity O(1)

def reverse_array(nums: List[int], left_idx: int, right_idx: int):
    l = left_idx
    r = right_idx
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        reverse_array(nums, 0, n-1)
        reverse_array(nums, 0, k-1)
        reverse_array(nums, k, n-1)



# Add solution with cyclic replacement
