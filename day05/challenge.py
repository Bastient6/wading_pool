import random
import time

def my_sort(list_ellement):
    max = 0
    index_max = 0
    new_list = [0 for i in range(10)]
    for i in range(len(list_ellement)):
        max = 0
        if list_ellement[i] > max:
            max = list_ellement[i]
            index_max = i
        list_ellement[index_max] = '\0'
        new_list[i] += max
    print(new_list)
    return new_list


def random_int():
    start = time.time()
    list_int = [random.randint(-32768, 32767) for i in range(10)]
    list_int = my_sort(list_int)
    print(time.time()- start)