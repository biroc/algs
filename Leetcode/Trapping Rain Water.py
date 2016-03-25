class Solution(object):
    def trap(self, height):
        max_rain = 0
        i = 0
        stack = []
        while i < len(height):
            if not stack or height[stack[-1]] > height[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if stack and height[stack[-1]] > height[top]:
                    rain_height = min(height[stack[-1]],height[i]) - height[top]
                    rain_width = i - stack[-1] - 1
                    max_rain += rain_height * rain_width

        return max_rain