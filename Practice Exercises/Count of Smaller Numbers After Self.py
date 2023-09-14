def count_smaller(nums):
    result = []
    sorted_nums = []
    for num in nums[::-1]:
        left, right = 0, len(sorted_nums)
        while left < right:
            mid = (left + right) // 2
            if sorted_nums[mid] >= num:
                right = mid
            else:
                left = mid + 1
        result.append(left)
        sorted_nums.insert(left, num)
    return result[::-1]

array = [5, 2, 6, 1]
result = count_smaller(array)
print(result)
