class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        # Reverse the list of words
        reversed_words = words[::-1]
        print(reversed_words)
        # Join the reversed words with spaces
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string        
        

Solution = Solution()

Solution.reverseWords("the sky is blue")
