import task11

def concat_first_letter(string):
    i = 0
    new = ""
    while i != len(string):
        new += string[i]
        while i + 1 != len(string) and string[i] != " ":
            i += 1
        i += 1
    return new

def make_word():
    string = concat_first_letter(string)
    print(string)

make_word()

    