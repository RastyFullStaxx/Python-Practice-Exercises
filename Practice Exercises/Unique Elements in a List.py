# Create a function that returns a list of unique elements from a given list.
def unique_elements(input_list):
    return list(set(input_list))

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(my_list)
print(unique_list)
