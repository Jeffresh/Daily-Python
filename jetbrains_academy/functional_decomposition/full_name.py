# In the code template below, you can see a program that creates a full name from the first and last names for
# several people. Wouldn't it be much easier if we had a function that could do the same?
#
# Your task is to create the function create_full_name that takes name and last_name (in this order) and returns
# the full name. Then redefine the full name variables using this function.
#
# Do NOT change the variable names.


def create_full_name(name, last_name):
    return name + " " + last_name


if __name__ == '__main__':
    name1 = "John"
    last_name1 = "Lennon"
    full_name1 = create_full_name(name1, last_name1)

    name2 = "Hermione"
    last_name2 = "Granger"
    full_name2 = create_full_name(name2, last_name2)

    name3 = "Lady"
    last_name3 = "Gaga"
    full_name3 = create_full_name(name3, last_name3)
