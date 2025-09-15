def del_dup_list(list_element):
    j = len(list_element) - 1
    for i in range(j):
        if i < j and list_element.count(list_element[i]) > 1:
            del(list_element[i])
            j -= 1
            i -= 2
    print(list_element)
del_dup_list(['a', 2, 'a', 2, 'A'])