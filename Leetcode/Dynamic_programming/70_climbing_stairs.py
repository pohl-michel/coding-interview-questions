class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)

    def iterative_climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            aux = [0]*(n+1)
            aux[0] = 1
            aux[1] = 1
            for k in range(2,n+1):
                aux[k] = aux[k-1] + aux[k-2]
            return aux[n]

    def better_iterative_climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            prev = 1
            crt = 1
            for _ in range(2,n+1):
                crt, prev = crt + prev, crt
            return crt         


test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_sol = Solution()
for elt in test_array:
    print(my_sol.climbStairs(elt))

for elt in test_array:
    print(my_sol.iterative_climbStairs(elt))

for elt in test_array:
    print(my_sol.better_iterative_climbStairs(elt))

# Rk: this is a linear recurrent relationship of order 2, 
# so this problem has a closed-form mathematical solution.
# Some explanations here: https://www.youtube.com/watch?v=Y0lT9Fck7qI 