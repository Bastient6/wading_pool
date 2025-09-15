def reverse_list(list_ellement):
    new_list = []
    for i in range(len(list_ellement) - 1, -1, -1):
        new_list.append(list_ellement[i])
    return new_list