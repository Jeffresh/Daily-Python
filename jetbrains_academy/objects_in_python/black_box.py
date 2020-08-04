# There's a function blackbox(lst) that takes a list, does some magic, and returns a list. You don't know if it
# modifies the given list or creates a completely different one. Find this out testing the function on your own list
# and print "modifies" if the function changes the given list or "new" if the returned list is not connected to the
# initial one.

if __name__ == '__main__':
    # use the function blackbox(lst) that is already defined
    my_list = [1, 3, 5]
    print("modifies" if my_list is blackbox(my_list) else "new")
