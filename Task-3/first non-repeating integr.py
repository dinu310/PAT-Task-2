def find_first_non_repeating_elements(input_list):
    element_dict = {}
    first_non_repeating_elements = []
    for element in input_list:
        if element in element_dict:
            element_dict[element] += 1
        else:
            element_dict[element] = 1
    for element in input_list:
        if element_dict[element] == 1:
            first_non_repeating_elements.append(element)
            break
    return first_non_repeating_elements

input_list = [1, 2, 3, 1, 3, 4, 5, 6, 7, 8, 9]
print(find_first_non_repeating_elements(input_list))