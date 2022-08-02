# Solution with sorting numbers
# time complexity O(n log n)
# space complexity O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        N = len(nums)
        if N == 1:
            return nums[0]
        
        nums = sorted(nums)
        nb_distinct_nums = N//2 +1 
            # if N = 5,  nb_distinct_nums = 3
        for i in range(nb_distinct_nums-1):
            if nums[2*i] != nums[2*i+1]:
                return nums[2*i]
        return nums[N-1]



# Solution with hashmap
# time complexity O(n)
# space complexity O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        min_num = min(nums)
        max_num = max(nums)
        counts = [0] * (max_num - min_num + 1)

        for num in nums:
            counts[num - min_num] += 1

        for num, count in enumerate(counts):
            if count == 1:
                return num + min_num



# similar solution using a dictionary with a better space usage:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                del counts[num]

        return list(counts.keys())[0]


            
# Solution using XOR
# time complexity O(n)
# space complexity O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

            result = 0
            for num in nums:
                result = num ^ result
            return result