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

def exercise2():
    res =     print(res)


if __name__ == "__main__":
    a = 2.0
    b = 5
    r = a / b
    fr, nu = math.modf(r)
    fr = f"{fr:.6f}"
    plusMinus([55, 48, 48, 45, 91, 97, 45, 1, 39, 54, 36, 6, 19, 35, 66, 36, 72, 93, 38, 21, 65, 70, 36, 63, 39, 76, 82, 26, 67, 29, 24, 82, 62, 53, 1, 50, 47, 65, 67, 19, 66, 90, 77])

