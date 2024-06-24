import math


# Lists comprehention
def parts(arr):
    res = [0, 0, 0]
    res[0] = len([e for e in arr if e > 0])
    res[1] = len([e for e in arr if e < 0])
    res[2] = len([e for e in arr if e == 0])
    return res


# math.modf => fractional part, integer part
def plusMinus(arr):
    # Write your code here
    splits = parts(arr)
    for e in splits:
        r = float(e) / len(arr)
        fr, nu = math.modf(r)
        print(f"{r:.6f}")

# sort list
# min, max sum of elements
def min_max(arr):
    arr.sort()
    print("%d %d" % (sum(arr[:4]), sum(arr[1:])))

# Sort reverse list
def sort_list():
    l = [5, 1, 3, 2]
    l.sort(reverse=True)


def exercise2():
    res = print(res)


if __name__ == "__main__":
    a = 2.0
    b = 5
    r = a / b
    fr, nu = math.modf(r)
    fr = f"{fr:.6f}"
    min_max([2,1,5, 3, 4])

