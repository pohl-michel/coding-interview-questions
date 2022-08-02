class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        k = 1  # number of distinct values, updated at each step in the loop

        if N != 1:

            i = 0
            while i < N - 1:
                if nums[i] != nums[i + 1]:
                    nums[k] = nums[i + 1]
                    k += 1
                i += 1

        return k