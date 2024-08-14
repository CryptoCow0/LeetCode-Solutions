import re

class Solution:
        
  


    def reverseVowels(self, s: str) -> str:
        # Define a regex pattern to match all vowels
        pattern = r"[aeiouAEIOU]"

        # Find all vowels in the string
        vowels = re.findall(pattern, s)

        # Reverse the list of vowels
        reversed_vowels = vowels[::-1]

        # Function to replace each vowel with the next one from reversed_vowels
        def replace_vowel(match):
            return reversed_vowels.pop(0)

        # Substitute the vowels in the original string with the reversed vowels
        result = re.sub(pattern, replace_vowel, s)

        return result

    # Example usage

        
solution = Solution()
result = solution.reverseVowels("Hello World")
print(result)
