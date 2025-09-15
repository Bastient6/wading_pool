import task13

def add_at_the_end_11_to_21(list_element):
    for i in range(11, 22):
        list_element = task13.add_element_on_list(list_element, i, len(list_element))
    return list_element
