class Solution:
  def flowerGame(self, n: int, m: int) -> int:
    xEven = n // 2
    yEven = m // 2
    xOdd = (n + 1) // 2
    yOdd = (m + 1) // 2
    return xEven * yOdd + yEven * xOdd