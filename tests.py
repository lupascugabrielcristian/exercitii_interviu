def each_element_in_array():
    a = [1, 2, 3]
    for e in a:
        print(e)


def lists_comprehention():
    a = [-2, -1, 0, 1, 2]
    b = [e for e in a if e < 0]
    print(b)


def sort_list():
    l = [5, 1, 3, 2]
    l.sort(reverse=True)
    print(l)

def string_contains():
    a = "hh:mm:ssAM"
    print(a[3:8])


l = [2,1]
print(l[1:])
