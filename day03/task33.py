import task11
def number_sum():
    task11.print_string("donne moi deux nombres")
    number1 = input()
    number2 = input()
    number = int(number1) + int(number2)
    task11.print_string(number)

number_sum()