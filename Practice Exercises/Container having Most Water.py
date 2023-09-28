def max_area(height):
    left, right = 0, len(height) - 1
    max_volume = 0

    while left < right:
        min_height = min(height[left], height[right])
        width = right - left
        volume = min_height * width
        max_volume = max(max_volume, volume)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_volume

# Example usage
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(heights)
