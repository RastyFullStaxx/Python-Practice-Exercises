def largest_unique_number(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    unique_nums = [num for num, count in counts.items() if count == 1]
    if unique_nums:
        return max(unique_nums)
    else:
        return -1

numbers = [5, 7, 3, 9, 4, 9, 8, 3]
result = largest_unique_number(numbers)
print(result)
