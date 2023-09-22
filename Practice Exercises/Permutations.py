def permute(nums):
    if not nums:
        return [[]]

    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i + 1:]
        for p in permute(rest):
            result.append([nums[i]] + p)

    return result

input_list = [1, 2, 3]
result = permute(input_list)
