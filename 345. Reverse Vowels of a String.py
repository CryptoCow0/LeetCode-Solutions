class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels for quick lookup
        vowels = set("aeiouAEIOU")
        
        # Convert the string to a list of characters
        s_list = list(s)
        
        # Initialize two pointers
        left, right = 0, len(s_list) - 1
        
        # Swap vowels using two-pointer technique
        while left < right:
            # Move left pointer to the next vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # Move right pointer to the previous vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # Swap vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        # Convert the list back to a string
        return ''.join(s_list)
