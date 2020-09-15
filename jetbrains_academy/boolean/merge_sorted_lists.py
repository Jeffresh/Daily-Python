# The merge_arrays(a, b) function, which is partly implemented below, takes two sorted lists of integers,
# merges them into one sorted list, and returns the result. The function should work in the following way:
# create an empty list c which will store the result; keep finding the smallest remaining
# element in a and b and moving it to the list c; stop when there are no elements left in a and b.
#
# Your task is to fill in the gaps so that the function works correctly. Note, that during the execution
# any of the lists a and b can become empty, so handle these cases carefully. Try to use non-boolean
# values in logical expressions when possible.
#
# Your program shouldn't read any input or call the function, just implement it.

def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    while a or b:
        if not b or a and a[0] < b[0]:
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c


if __name__ == '__main__':
    print(merge_arrays([1, 3, 6, 7], [0, 2, 5]))
