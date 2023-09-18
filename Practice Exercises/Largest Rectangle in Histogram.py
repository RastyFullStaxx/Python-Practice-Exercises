def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

    while stack:
        top = stack.pop()
        width = index if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[top] * width)

    return max_area

histogram = [2, 1, 5, 6, 2, 3]
result = largest_rectangle_area(histogram)
print(result)
