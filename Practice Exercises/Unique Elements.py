def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = remove_duplicates(my_list)
print(unique_elements)
