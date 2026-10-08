#You are climbing a staircase. It takes n steps to reach the top. Each time you can climb either 1 or 2 steps. How many distinct ways can you reach the top?
#Example:
#Input:  n = 5
#Output: 8

def climbing_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climbing_stairs(5))  # Output: 8