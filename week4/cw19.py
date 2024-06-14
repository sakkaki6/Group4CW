import itertools as it


def combination(input):
    l1 = list(input)
    for r in range(1, len(input)+1):
        list1 = (it.combinations(l1, r))
        [print(item) for item in list1]


combination('123')
