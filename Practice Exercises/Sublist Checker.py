def is_sublist(sublist, mainlist):
    n, m = len(sublist), len(mainlist)
    for i in range(m - n + 1):
        if mainlist[i:i + n] == sublist:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6]
sub_list1 = [2, 3, 4]
sub_list2 = [4, 5, 6, 7]

print(is_sublist(sub_list1, main_list))
print(is_sublist(sub_list2, main_list))
