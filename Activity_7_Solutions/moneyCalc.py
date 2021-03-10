def totalMoney(n):
    q, r = divmod(n - 1, 7)
    # q : total number of completed weeks
    # r : day (0 indexed) of the last week that wasnt completed
    # O(1) solution 
    ans = 28 * q + q * (q - 1) * 7 // 2
    ans += (r + 1) * (r + 2) // 2
    ans += q * (r + 1)
    return ans

print(totalMoney(10))

