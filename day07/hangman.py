import random
from english_words import get_english_words_set

def loose(penalty):
    if penalty >= 12:
        print("You loose!")
        return False
    return True

def rand():
    new_set = set("123456")
    i = random.randint(0, len(new_set))
    return new_set[i]

def update_string(string, letter, current_string):
    new_current_string = ""
    for i in range(len(string)):
        for j in range (len(letter)):
            if string[i] == letter[j]:
                new_current_string += string[i]
        if len(new_current_string) <= i:
            new_current_string += current_string[i]
            
    return new_current_string

def make_underscore(string):
    new_string =""
    for i in range(len(string)):
        new_string += "_"
    return new_string
    
def print_underscore(string):
    print(string, end=" ")

def find_underscore(string):
    for i in range(len(string)):
        if string[i] == "_":
            return True
    return False

def find_letter(string, letter):
    if letter in string:
        if len(letter) == 1:
            print ("Found '"+letter +"'")
        else:
            print(letter + ": correct guess")
        return 0
    if len(letter) == 1:
        print ("Not found '"+letter +"'")
        return 1
    else:
        print(letter + ": incorrect guess")
        return len(letter)

def hangman():
    status = 0
    penalty = 0
    words = get_english_words_set(['web2'], lower=True)
    word = random.choice(list(words))
    current_string = make_underscore(word)
    while status != 1:
        letter = input()
        penalty += find_letter(word, letter)
        current_string = update_string(word, letter, current_string)
        if loose(penalty) == False:
            status = 1
            return
        print_underscore(current_string)
        if find_underscore(current_string) == False:
            print("/ YOU WIN!")
            status = 1
            return
        print("/ ", end="")
        print(penalty, end="")
        if penalty <= 1:
            print("penalty")
        else:
            print("penalties")


hangman()