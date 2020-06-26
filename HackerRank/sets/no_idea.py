# There is an array of integers. There are also 2 disjoint sets, A and B, each containing m integers.
# You like all the integers in set A and dislike all the integers in set B .
# Your initial happiness is 0 . For each i integer in the array, if i in A , you add 1 to your happiness. If i in B ,
# you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
#
# Note: Since A and B and are sets, they have no repeated elements. However, the array might contain duplicate elements.

def happiness(array, set_a, set_b):
    happiness_ = sum((x in set_a) - (x in set_b) for x in array)
    print(happiness_)


if __name__ == '__main__':
    size_array, size_sets = map(int, ['2', '3'])
    array = list(map(int, ['1', '5', '3']))
    set_a = set(map(int, ['3', '1']))
    set_b = set(map(int, ['5', '7']))

    happiness_ = [1 for x in array if x in set_a]
    not_happiness = [-1 for x in array if x in set_b]
    print(sum(happiness_ + not_happiness))

    happiness(array, set_a, set_b)
