import task31

def passcheck(fun, n, s ):
    if isinstance(n, int) == False:
        print("bad argument n")
        return False
    if isinstance(s, str) == False:
        print("bad argument s")
        return False
    return fun(s, n)

def check():
    if passcheck(task31.funA, 16, "mysecretpassword") == True:
        if passcheck(task31.funB, 3, "mysecretpassword") == True:
            if passcheck(task31.funC, 1, "mysecretpassword") == True:
                print("good password")
                return
            print("bad password")
            return
        print("bad password")
        return
    print("bad password")

check()