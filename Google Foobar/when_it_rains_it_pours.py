def answer(heights):
    if not heights:
        return 0
    stack = []
    total_area = i = 0
    while i < len(heights):
        if not stack or heights[i] < heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack:
                height = min(heights[i] - heights[top],heights[stack[-1]] - heights[top])
                width = i - stack[-1] - 1
                total_area += (height * width)

    return total_area