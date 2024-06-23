def each_element_in_array():
    a = [1, 2, 3]
    for e in a:
        print(e)


def lists_comprehention():
    a = [-2, -1, 0, 1, 2]
    b = [e for e in a if e < 0]
    print(b)

lists_comprehention()