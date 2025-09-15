def print_element_index(list_element, index):
    if index > len(list_element):
        print("l'index est en dehors de la liste")
        return
    print(list_element[index - 1])
