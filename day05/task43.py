list_name = [
    ["Monday", "3:30 PM", "Joe", "Sam"],
    ["Monday", "4:30 PM", "Bob", "Alice"],
    ["Tuesday", "3:30 PM", "Joe", "Bob", "Alice", "Sam"],
    ["Tuesday", "9:30 AM", "Joe", "Bob"]
]

def meeting():
    name = input("what is your name ?:\n")
    for i in range(len(list_name)):
        if list_name[i].count(name) >= 1:
            print(list_name[i][0] + " "+ list_name[i][1])

meeting()