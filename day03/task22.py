def tu_to_ta(string):
    new = ""
    index = 0
    while index != len(string):
        if (string[index] == 't' and index + 1 != len(string) and string[index + 1] == 'u'):
            new += string[index]
            new += 'a'
            index += 1
        else :
            new += string[index]
        index += 1
    return new
