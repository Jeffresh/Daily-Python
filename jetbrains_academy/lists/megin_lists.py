# Write a function that would take two lists and return one merged list, e.g.
# for the lists ['Washington, D.C.', 'Chicago', 'New York'] and ['Los Angeles', 'Las Vegas']
# the result should be ['Washington, D.C.', 'Chicago', 'New York', 'Los Angeles', 'Las Vegas'].
#
# You can use any of the methods described in the theory.

def merge_lists(list_one, list_two):
    return list_one + list_two


if __name__ == '__main__':
    list_a = [1, 2, 5]
    list_b = ['a', 'b', 'c']

    print(merge_lists(list_a, list_b))
