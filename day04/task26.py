import task12

def print_2_to_ndiv2():
    n = task12.ask_integer()
    j = 2
    while j != n // 2 + 1:
        for i in range(n - 1, j - 1, -1):
            if i % j== 0:
                print(i, end=" ")
        j+=1
        print("")
