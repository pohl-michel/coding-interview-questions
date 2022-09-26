class Solution:
    def myAtoi(self, s: str) -> int:
        
        POS = True
        N = len(s)
        my_nb = 0
        
        if N != 0:
                      
            crt_idx = 0
            while crt_idx < N and s[crt_idx] == " ":
                crt_idx += 1
                
            if crt_idx < N and s[crt_idx] == "-":
                POS = False
                crt_idx += 1
            elif crt_idx < N and s[crt_idx] == "+":
                crt_idx += 1
            
            srtidx = crt_idx

            while crt_idx < N and s[crt_idx] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                crt_idx += 1

            if srtidx != crt_idx:

                my_nb = int(s[srtidx:crt_idx])

                if not POS:
                    my_nb = - my_nb

                if my_nb >= 2**31:
                    my_nb = 2**31 - 1
                if my_nb < -2**31:
                    my_nb = -2**31

        return my_nb
                
mysol = Solution()
my_strings = ["42", "   -42", "4193 with words", "9999999999999999999999999999999999999999999999999999999999"]
for my_string in my_strings:
    print(mysol.myAtoi(my_string))

print(2**31) # for checking


# Solution on Youtube (Google Engineer Explains): 
# https://www.youtube.com/watch?v=zwZXiutgrUE
#
# The development at the end regarding languages where there IS a max integer and min integer is important.