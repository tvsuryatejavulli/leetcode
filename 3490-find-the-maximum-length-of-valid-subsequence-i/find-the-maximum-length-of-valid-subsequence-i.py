class Solution:
  def maximumLength(self, nums: list[int]) -> int:
    dp = [[0] * 2 for _ in range(2)]

    for x in nums:
      for y in range(2):
        dp[x % 2][y] = dp[y][x % 2] + 1

    return max(map(max, dp))