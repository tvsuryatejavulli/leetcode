class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        heights.pop()
        return max_area
