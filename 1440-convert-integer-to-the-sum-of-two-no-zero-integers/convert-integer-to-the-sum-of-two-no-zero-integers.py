class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(n):
            y=n-x
            if '0' not in str(x) and '0' not in str(y):
                return x,y
