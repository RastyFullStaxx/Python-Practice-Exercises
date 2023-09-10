def two_sum(nums, target):
    num_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], i]
        num_index[num] = i
    return []

numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
