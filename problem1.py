nums = input()
nums = nums.split(',')
nums = [int(x) for x in nums]
nums = [1] + nums + [1]
n = len(nums)
dp = [[0 for n in range(n)] for j in range(n)]

for k in range(2,n):
	for left in range(0, n-k):
		right = left + k
		for i in range(left+1,right):
			dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

print(dp[0][n-1])