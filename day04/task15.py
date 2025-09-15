import task12
import task13

def comp_int():
    integer = task12.ask_integer()
    if task12.is_equal_to(integer, 42):
        print("a")
    if integer <= 21:
        print("b")
    if task13.odd_even(integer):
        print("c")
    if integer / 2 <= 21: 
        print("d")
    if task13.odd_even(integer) == False and integer >= 45:
        print("e")
    else :
        print("f")
    