
def is_equal_to(number, target):
    if number == target:
        return True
    return False

def print_is_equal(status):
    if status:
        return print("This is correct!")
    return print("This is not equal to 42")

def ask_integer ():
    print("écris un entier:")
    integer = int(input())
    return integer
