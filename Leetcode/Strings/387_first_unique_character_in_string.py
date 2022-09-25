class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
                
        for idx, char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1


my_string = "loveleetcode"
sol = Solution()
print(sol.firstUniqChar(my_string))
