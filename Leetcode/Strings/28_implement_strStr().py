class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # n = 3
        # m = 2
        # i_start in range(2) 2 = 3 - 2 + 1

        n = len(haystack)
        m = len(needle)
        for i_start in range(n - m + 1):
            if haystack[i_start:(i_start+m)] == needle:
                return i_start
        return -1

mysol = Solution()

examples = [("sadbutsad", "sad"), ("leetcode", "leeto"), ("abracadabra", "bra")]

for haystack, needle in examples:
    print(mysol.strStr(haystack, needle))

# Rk 1: "if haystack[i_start:(i_start+m)] == needle" could be replaced by an inner loop
# Rk 2: the Knuth-Morris-Pratt algorithm: https://www.youtube.com/watch?v=JoF0Z7nVSrA
# Basically reinventing the KMP algorithm in itself is very hard, but one should be able to:
# - efficiently implement code to find the longest prefix suffix (LPS)
# - understand how that brick of code helps find matching substrings