class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        m = len(word1)
        n = len(word2)
        result = []  # Using a list for efficient appending
        i = 0
        j = 0

        while i < m or j < n:
            if i < m:
                result.append(word1[i])
                i += 1
            if j < n:
                result.append(word2[j])
                j += 1
        
        return "".join(result) # Join the list to form a string