
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # Length of the string
      
        # Table to store the palindrome status
        # dp[i][j] will be 'True' if the string from index i to j is a palindrome.
        dp = [[True] * n for _ in range(n)]
      
        start_index = 0  # Start index of the longest palindrome found
        max_length = 1   # Length of the longest palindrome found, initially 1 character
      
        # Bottom-up dynamic programming approach.
        # Start from the end of the string and move towards the beginning.
        for i in range(n - 2, -1, -1):  # i is the start index of the substring
            for j in range(i + 1, n):  # j is the end index of the substring
                dp[i][j] = False  # Initially set to False
              
                # Check if the current substring is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True  # Update the palindrome status
                    # Check if the current palindrome is the longest found so far
                    if max_length < j - i + 1:
                        start_index = i
                        max_length = j - i + 1  # Update max_length
      
        # Return the longest palindrome substring
        return s[start_index : start_index + max_length]
