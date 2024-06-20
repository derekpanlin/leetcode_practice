# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. 
# If it is impossible to form any triangle of a non-zero area, return 0.


# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:


# Input: nums = [1,2,1,10]
# Output: 0
# Explanation: 
# You cannot use the side lengths 1, 1, and 2 to form a triangle.
# You cannot use the side lengths 1, 1, and 10 to form a triangle.
# You cannot use the side lengths 1, 2, and 10 to form a triangle.
# As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

# Constraints:

# 3 <= nums.length <= 10**4
# 1 <= nums[i] <= 10**6

# POLYAS
# 1) Order the list from smallest to largest
#  Input: nums = [1,1,2,10]
# 2) Iterate  assigning a, b, and c to sequential indices
# 3) Check if b + c > a 
#   a) If yes, store the maximum perimeter and return it
#   b) If no, return zero

def largest_perimeter(nums):
    nums.sort(reverse=True)
    
        
    for i in range(len(nums)-2):
        a = nums[i]
        b = nums[i+1]
        c = nums[i+2]

    
        # Check if b + c > a
        if a < b + c:
            return a + b + c
        
    return 0


nums = [3,2,3,4]
print(largest_perimeter(nums))
