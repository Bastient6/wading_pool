import task11

def upper_first(string):
    new = ""
    if (string[0] >= 'a' and string[0] <= 'z'):
            new += chr(ord(string[0]) - 32)
    for index in range (1, len(string)):
        if (string[index] >= 'A' and string[index] <= 'Z'):
            new += chr(ord(string[index]) + 32)
        else :
            new += string[index]
    return new

def hello():
    task11.print_string("quel est ton nom?")
    name = input()
    name = upper_first(name)
    task11.print_string("Hello " + name)

hello()