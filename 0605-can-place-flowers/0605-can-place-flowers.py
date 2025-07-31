class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # A simple check to handle the case where n is already 0
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the left plot is empty or at the beginning
                is_left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                
                # Check if the right plot is empty or at the end
                is_right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both adjacent plots (or edges) are empty, we can plant a flower
                if is_left_empty and is_right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    
                    # If we've planted all the required flowers, return True
                    if n == 0:
                        return True
        
        # If the loop finishes and n is still greater than 0, we couldn't plant all flowers
        return False