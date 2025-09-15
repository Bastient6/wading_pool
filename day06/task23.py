import os
def ls_R(rep):
    files = os.listdir(rep)
    for file in files:
        path = os.path.join(rep, file)
        print(path)
        if (os.path.isdir(path)):
            ls_R(path)

ls_R("../")