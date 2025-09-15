import task14

def print_twice():
    string = task14.ask_string()
    for i in range (len(string)):
        for j in range (2):
            print(string[i], end="")