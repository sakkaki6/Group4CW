import itertools as it


# def combination(string):
#     count = 0
#     permutations = it.permutations(string)
#     for perm in permutations:
#         count += 1
#         print(''.join(perm))
#     print(f"count of permutations : {count}")


# combination('ABC')

import itertools as it

def combination(string):
    [print(''.join(perm)) for perm in it.permutations(string)]

combination('ABC')
