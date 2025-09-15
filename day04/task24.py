# import task23

# def int_m30_to_30():
#     for i in range (30, -31, -1):
#         print(i)
#         if task23.is_multiple_of(i, 3):
#             print("Fizz", end="")
#         if task23.is_multiple_of(i, 5):
#             print("Buzz", end="")
#         print("")


for i in range(-30, 31):
    if i % 3 != 0 and i % 5 != 0:
        print(i, end = "")
    if i % 3 == 0:
        print("Fizz", end = "")
    if i % 5 == 0:
        print("Buzz", end = "")
    print("")
    