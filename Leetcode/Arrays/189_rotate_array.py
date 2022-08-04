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

# Similar solution in Java here:
# https://leetcode.com/problems/rotate-array/discuss/259418/Clear-cyclic-replacement-Java-solution-with-proof

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



# Solution with cyclic replacement
# The most intuitive but the most difficult to code
# time complexity O(n)
# memory complexity O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        visited_elt_count = 0
        n = len(nums)
        step = n - k
    
        cycle_start_idx = 0
        
        while visited_elt_count < n:
            
            crt_idx = cycle_start_idx
            next_idx = (crt_idx + k) % n

            hold = nums[crt_idx]
            
            while next_idx != cycle_start_idx:
                nums[next_idx], hold = hold, nums[next_idx]
                visited_elt_count += 1
                crt_idx = next_idx
                next_idx = (crt_idx + k) % n
            
            nums[next_idx] = hold
            visited_elt_count += 1
            cycle_start_idx += 1
