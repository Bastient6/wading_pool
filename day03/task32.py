import task11
def type_number():
    task11.print_string("donne moi un nombre")
    number = input()
    for index in range (0, len(number)):
        if (number[index] == '.' or number[index] == ','):
            task11.print_string("c'est un nombre flottant")
            return
    task11.print_string("c'est un nombre entier")

type_number()
    