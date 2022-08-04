# solution using sorting
# time complexity O(n log n)
# space complexity O(n) (because we need to create a new array to store intersection result)

# Rk: if the array is already sorted, we can reuse most of that code, and the memory utilization would be less than for the solution with the hashmap.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        
        i = 0
        j = 0
        
        while(i < n1 and j < n2):
    
            elt1 = nums1[i]
            elt2 = nums2[j]
    
            if elt1 < elt2:
                i += 1
            elif elt1 > elt2:
                j += 1
            else: #elt1 = elt2
                result.append(elt1)
                i += 1
                j += 1
        
        return result



# Solution using hashmap
# Time complexity O(n)
# Space complexity max(nums1, nums2)

# Rk: would have been better with a dictionary instead of a list for counts

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        m1 = max(nums1)
        m2 = max(nums2)
        m = max(m1,m2)
        counts = [0]*(m+1)
        result = []

        for elt in nums1:
            counts[elt] += 1
        for elt in nums2:
            if counts[elt] >0:
                result.append(elt)
                counts[elt] -= 1    

        return result