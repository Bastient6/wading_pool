import task12
def print_from_to(start, end, string):
    while start != end:
        task12.print_by_index(start - 1, string)
        start += 1