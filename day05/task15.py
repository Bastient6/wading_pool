def rm_element_index(list_element, index):
    i = 0
    new_list = []
    while i != index - 1:
        new_list.append(list_element[i])
        i += 1
    i += 1
    while i < len(list_element):
        new_list.append(list_element[i])
        i += 1
    return new_list
    
