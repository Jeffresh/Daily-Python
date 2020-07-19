# Below you can see the code that chooses some elements
# from one list and appends them to another:
#
# for a in x:
#     for el in a:
#         if el > 0:
#             els.append(el)
#
# Fill in the blanks in the code below so that list
# comprehension produces the same result as the code above.
import json

if __name__ == '__main__':
    # here we create the initial list from the input, please do not modify this line
    x = json.loads(input())

    els = [el for a in x for el in a if el > 0]
