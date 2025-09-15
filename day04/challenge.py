
vowel = ["a", "e", "i", "o", "u", "y"]

def ask_integer_and_sring():
    new_string = ""
    integer = 0
    i = 0
    string = input("écris un entier et une phrase\n")
    while string[i] != " ":
        integer = integer * 10 + int(string[i])
        i += 1
    for i in range(i + 1, len(string)):
        new_string += string[i]
    return integer, new_string

def challenge():
    integer, string = ask_integer_and_sring()
    if integer :
        if "t" in ["t" if vowel[i] in string else "f" for i in range (len(vowel))]:
            print(integer)
        if integer >= 42:
            print(integer)
        else :
            print(string)
