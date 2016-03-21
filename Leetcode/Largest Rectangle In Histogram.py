class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights: return 0
        max_area = i = 0
        stack = []
        while i < len(heights):
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                current_top = stack.pop()
                height = heights[current_top]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area,height*width)
        
        while stack:
            current_top = stack.pop()
            height = heights[current_top]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area,height*width)
        
        return max_area