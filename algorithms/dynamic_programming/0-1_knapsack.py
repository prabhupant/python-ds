# Dynamic Problem Solution for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W 

# wt = weight of elements.
# val = value of elements.
# n = number of elements.
# W = Maximum Weight.

def knapSack(W, wt, val, n): 
	dp = [[0 for x in range(W+1)] for x in range(n+1)] 

	# Build table dp[][] in bottom up manner 
	for i in range(n+1): 
		for w in range(W+1): 
            # base condition    
			if i==0 or w==0: 
				dp[i][w] = 0
			elif wt[i-1] <= w: 
				dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]) 
			else: 
				dp[i][w] = dp[i-1][w] 

	return dp[n][W] 