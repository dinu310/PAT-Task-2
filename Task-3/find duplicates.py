def find_duplicates(list1, list2, list3):
    combined_list = list1 + list2 + list3
    duplicate_dict = {}
    for num in combined_list:
        if num in duplicate_dict:
            duplicate_dict[num] += 1
        else:
            duplicate_dict[num] = 1
    duplicates = [num for num, count in duplicate_dict.items() if count > 1]
    return duplicates

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [5, 6, 7, 8, 9]

print(find_duplicates(list1, list2, list3))
