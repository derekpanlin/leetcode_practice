# 67. Add Binary
# Easy
# Topics
# Companies
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

def addBinary(a: str, b: str) -> str:
    # Find length of string and assign to variables
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []
    
    while i >= 0 or j >= 0:
        ai = int(a[i]) if i >= 0 else 0
        bi = int(b[j]) if j >= 0 else 0
        total = ai + bi + carry
        result.append(total % 2)
        carry = total // 2
        i -= 1
        j -= 1
    
    if carry:
        result.append(carry)
    
    return ''.join(str(bit) for bit in reversed(result))

# Test cases
print(addBinary("11", "1"))    # Output: "100"
print(addBinary("1010", "1011"))  # Output: "10101"
