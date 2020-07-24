# Ruth goes shopping today, so she is busy making a shopping list.
#
# She wrote down things that she would like to buy at the grocery store: first "milk", then "olive oil"
# and "bananas". When sneaking a look at the fridge, she noticed that there was some milk left and changed
# her mind about buying a new one. It got crossed out of the list. And, like a cherry on top, a "brownie" became
# the last item Ruth had put on the list.
#
# Now you try to replicate these operations on the variable shopping_list.
#
# You are NOT supposed to print the results.
#


if __name__ == '__main__':
    # work with this variable
    shopping_list = []

    shopping_list.append("milk")
    shopping_list.append("olive oil")
    shopping_list.append("bananas")
    shopping_list.remove('milk')
    shopping_list.append("brownie")