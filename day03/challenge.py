import task21
import task11

cat = "cat"
garden = "garden"
mice = "mice"

def find_cat(string, index, status):
    for i in range (0, 3, 1):
        if string[index + (i * status)] != cat[i]:
            return 0
    return 1

def find_garden(string, index, status):
    for i in range (0, 6, 1):
        if string[index + (i * status)] != garden[i]:
            return 0
    return 1

def find_mice(string, index, status):
    for i in range (0, 4, 1):
        if string[index + (i * status)] != mice[i]:
            return 0
    return 1

def occur(string):
    string = task21.to_lowercase(string)
    total = 0
    for i in range (0, len(string)):
        if string[i] == "c":
            total += find_cat(string, i, 1)
        if string[i] == "g":
            total += find_garden(string, i, 1)
        if string[i] == "m":
            total += find_mice(string, i, 1)
    for i in range (len(string) - 1, 0, -1):
        if string[i] == "c":
            total += find_cat(string, i, -1)
        if string[i] == "g":
            total += find_garden(string, i, -1)
        if string[i] == "m":
            total += find_mice(string, i, -1)
    task11.print_string(total)
