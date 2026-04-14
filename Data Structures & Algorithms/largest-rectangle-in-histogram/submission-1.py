class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][1]:
                index, num = stack.pop()
                largest = max(num * ((i) - index), largest)
            stack.append([index, h])
        while stack:
            index, num = stack.pop()
            largest = max(num * (len(heights) - index), largest)
        return largest