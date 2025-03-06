from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenation order matches, else return ""
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute GCD of the lengths
        gcd_length = gcd(len(str1), len(str2))
        print(gcd_length)
        
        # The common divisor string is the first gcd_length characters of str1
        return str1[:gcd_length]