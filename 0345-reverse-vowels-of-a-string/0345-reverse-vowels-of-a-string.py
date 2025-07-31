class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Define the set of vowels for efficient lookup
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Convert the string to a list of characters to make it mutable
        s_list = list(s)
        
        # Initialize two pointers
        left, right = 0, len(s_list) - 1
        
        while left < right:
            # Move the left pointer until a vowel is found
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # Move the right pointer until a vowel is found
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # If the pointers haven't crossed, swap the vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                
                # Move both pointers inward
                left += 1
                right -= 1
        
        # Join the list back into a string and return it
        return "".join(s_list)