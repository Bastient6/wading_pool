import task12

def veg_sandwish():
    task12.bread()
    for i in range(0, 2):
        task12.lettuce()
        task12.tomato()
    task12.bread()


def make_sandwish_with_option(status):
    if status == "veg":
        veg_sandwish()
        return
    task12.make_sandwich()

make_sandwish_with_option("veg")
make_sandwish_with_option("normal")
