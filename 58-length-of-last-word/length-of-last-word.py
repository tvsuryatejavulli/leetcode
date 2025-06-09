class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split()
        
        if not words:
            return 0
        
        last_word = words[-1]
        
        length = len(last_word)    
        return length
