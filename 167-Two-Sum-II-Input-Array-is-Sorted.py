''' Q-167: Two Sum II - Input array is sorted
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice. '''

 
def twoSumII(numbers, target):
    left = 0
    right = len(numbers)-1
    while left < right:
        total_sum = numbers[left] + numbers[right]
       
        if total_sum == target:
            return([left+1, right+1])
        elif total_sum > target:
            right -= 1
        else:
            left += 1

numbers=[1,3,4,5]
target = 5
print(twoSumII(numbers,target))

#Output - [1,3]
