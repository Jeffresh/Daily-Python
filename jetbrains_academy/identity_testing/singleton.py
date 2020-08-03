# Jules has just discovered singletons and decided to experiment with None, True and False. As you know,
# these objects are created once in the runtime of a program.
#
# Jules saved truthy and falsy values to variables, but forgot to set the None value to a variable none_obj.
# Fix this mistake!
#
# Also, revise the rest of the code to see that all # Truthy values have the same identity as True, while all #
# Falsy values are indeed False. To achieve this, convert the values via the built-in bool() function, e.g.
# one = bool(1). Use this function for other statements as well.
#
# You are NOT supposed to print anything.

if __name__ == '__main__':
    # Truthy values
    one = bool(1)
    non_empty_string = bool("singleton")

    # Falsy values
    zero = bool(0)
    empty_list = bool([])

    # NoneType
    none_obj = None
