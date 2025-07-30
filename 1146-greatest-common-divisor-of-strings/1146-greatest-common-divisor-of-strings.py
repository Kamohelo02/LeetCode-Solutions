class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Helper function for GCD (Euclidean algorithm)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Step 1: Check the concatenation property
        # If str1 + str2 != str2 + str1, then no common divisor string exists.
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Calculate the GCD of the lengths of str1 and str2
        # The length of the greatest common divisor string will be gcd(len(str1), len(str2)).
        len1 = len(str1)
        len2 = len(str2)
        
        # Use our custom gcd helper function
        gcd_length = gcd(len1, len2)
        
        # Step 3: Extract the potential GCD string
        # The GCD string is the prefix of str1 (or str2) of length gcd_length.
        return str1[:gcd_length]