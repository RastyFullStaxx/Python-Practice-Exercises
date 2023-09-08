def partition_list(lst, value):
    less_than = []
    greater_than_or_equal = []
    for item in lst:
        if item < value:
            less_than.append(item)
        else:
            greater_than_or_equal.append(item)
    return less_than, greater_than_or_equal

my_list = [3, 7, 1, 5, 9, 2, 8]
value = 5
less, greater_equal = partition_list(my_list, value)
print(f"Less than {value}: {less}")
print(f"Greater than or equal to {value}: {greater_equal}")
