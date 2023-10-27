# Write a function to flatten a nested list.
def flatten_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list

nested_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = flatten_list(nested_list)
print(flattened_list)
