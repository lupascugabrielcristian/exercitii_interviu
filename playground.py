import math

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


def breakingRecords(scores):
    _min = [scores[0], 0]
    _max = [scores[0], 0]
    for n in scores:
        if n < _min[0]:
            _min[0] = n
            _min[1] += 1
        if n > _max[0]:
            _max[0] = n
            _max[1] += 1

    return [_min[1], _max[1]]


def divisibleSumPairs(n, k, ar):
    res = 0
    for i in ar:
        for j in ar:
            if i < j and (i+j) % k == 0:
                res += 1
    return res

def migratoryBirds(arr):
    sightings = {}
    for e in arr:
        if e in sightings:
            sightings[e] +=1
        else:
            sightings[e] = 1
    sightings = list(sightings.items())
    sightings.sort()

    max = sightings[0][1]
    id = sightings[0][0]
    for s in sightings:
        if s[1] > max:
           id = s[0] 

    return id

# r = migratoryBirds([1, 1, 2, 2, 3])
# r = migratoryBirds([1, 4, 4, 4, 5, 3])
r = migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
print(r)