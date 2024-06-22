# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# POLYAS
# Create a for loop to track 1st num
# Create a for loop to track 2nd num
# Check if curr nums add to target 
# Output indices of curr nums

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# After submitting and clearing, you want to see if you can optimize
# Memoization method - caching results and returning them when needed to optimize run time
# POLYAS
# Create a for loop to go through every number
# Create var to store visited nums
# Check to see if the difference of the curr num has already been visited
# Output indices

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_search = {}
        
        for i in range(len(nums)):
            if not nums[i] in diff_search:
                diff_search[target - nums[i]] = i
            else:
                return [diff_search[nums[i], i]]
