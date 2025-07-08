class Solution:
  def maxValue(self, events: list[list[int]], k: int) -> int:
    events.sort()

    @functools.lru_cache(None)
    def dp(i: int, k: int) -> int:
      if k == 0 or i == len(events):
        return 0
        
      j = bisect.bisect(events, [events[i][1], math.inf, math.inf], i + 1)
      return max(events[i][2] + dp(j, k - 1), dp(i + 1, k))

    return dp(0, k)