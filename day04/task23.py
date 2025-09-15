def is_multiple_of(integer, target):
    if integer % target == 0:
        return True
    return False

def print_decreasingly_div_by_7():
    for i in range(10000, 0, -1):
        if is_multiple_of(i, 7):
            print(i)
# [print(i) for i in range(10000, 0, -1) if i%7 == 0]