'''
Q-1: Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.'''

# Brute Force - O(n^2)
def two_sum_brute(nums, target):
	for i in range(len(nums)-1):
		finalList=[]
		for j in range(i+1, len(nums)):
			if nums[i]+nums[j] == target:
				return([i,j])

# Optimized approach - O(n)
def two_sum_hashMap(nums,target):
	hashMap={}
	for i in range(len(nums)):
		if (nums[i] in hashMap):
			return ([i, hashMap[nums[i]]])
		hashMap[target-nums[i]] = i


nums = [1,2,5,4] 
target = 7
print(two_sum_brute(nums,target))
print(two_sum_hashMap(nums,target))

#Output - [1,2] 