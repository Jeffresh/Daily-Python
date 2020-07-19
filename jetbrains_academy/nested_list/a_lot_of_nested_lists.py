# Let's write a program that will read a positive integer n from
# the input and create a nested list
# containing the inner list [1, 2] repeated n times.

if __name__ == '__main__':
    n = int(input())

    my_list = [[1, 2] for _ in range(n)]
    # or
    my_list = [[1, 2]] * 2

    print(my_list)
