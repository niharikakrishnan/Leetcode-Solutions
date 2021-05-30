''' 1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''
#Time Complexity - O(n)
def runningSum(nums):
	totalSum = 0
	result=[]
	for i in nums:
		totalSum = totalSum + i
		result.append(totalSum)
	return result

nums=[1,2,3,4]
print(runningSum(nums))

#Output - [1,3,6,10]