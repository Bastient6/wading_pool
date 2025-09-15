import task12

def make_n_sandwishes(n):
    if isinstance(n, int) == False or n <= 0:
        print("I can't do this")
        return 
    for i in range(0,n):
        task12.make_sandwich()
make_n_sandwishes(1.2)