n = int(input())
nums = input()
nums = nums.split()
nums = [int(x) for x in nums]
#print(nums,n)

sums = {}
for n1 in range(len(nums)):
	for n2 in range(n1+1, len(nums)):
		num1, num2 = nums[n1], nums[n2]
		if num1+num2 in sums: sums[num1+num2] += 1
		else: sums[num1+num2] = 1
#print(sums)
nways = 0
for n in nums:
	if n in sums: nways += sums[n]
print(nways)
