'''Q11 - Container-With-Most-Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.'''

# TimeComplexity - O(n^2) - Time Limit Exceeded Error
def maxArea_BruteForce(height): 
    maxArea = 0
    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j-i)
            if area>maxArea:
                maxArea = area
    return maxArea

# TimeComplexity - O(n) - All Test Cases Passed
def maxArea_twoPointer(height):
    left = 0
    right = len(height)-1
    maxArea=0
    while left < right:              
        if height[left] <= height[right]:
            area = height[left] * (right-left)
            left = left + 1
        else:
            area = height[right] * (right-left)
            right = right - 1
        if area > maxArea:
            maxArea = area
    return maxArea
        
#Further optimization by checking for max height