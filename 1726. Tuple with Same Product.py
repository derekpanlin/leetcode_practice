# # https://leetcode.com/problems/tuple-with-same-product/description/


# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# All elements in nums are distinct.

# POLYAS
# 

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_count = {}
        num_of_tuples = 0
        
        # Calculate all possible products and store their indices
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_count:
                    product_count[product].append((i, j))
                else:
                    product_count[product] = [(i,j)]
        
        # Count tuples (a, b, c, d) where a * b = c * d
        
        for pairs in product_count.values():
            m = len(pairs)
            for i in range(m):
                for j in range(i + 1, m):
                    (a, b), (c, d) = pairs[i], pairs[j]
                    if a != b and a != c and a != d and b != c and b !=d:
                        num_of_tuples += 8
                
        
        return num_of_tuples
