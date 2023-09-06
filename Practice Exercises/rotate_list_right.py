def rotate_list_right(lst, positions):
    positions = positions % len(lst)
    return lst[-positions:] + lst[:-positions]

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list_right(my_list, 2)
print(rotated_list)
