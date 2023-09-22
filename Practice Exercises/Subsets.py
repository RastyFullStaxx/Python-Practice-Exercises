def subsets(nums):
    result = [[]]

    for num in nums:
        result += [curr + [num] for curr in result]

    return result

input_set = [1, 2, 3]
result = subsets(input_set)
