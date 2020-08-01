def LIS(arr):
    n = len(arr)
    if n == 0: return 0
    res = 1
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n): 
        dp[i] = 1; 
        for j in range(0 , i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i] , dp[j] + 1)
        res = max(res , dp[i])
    return res