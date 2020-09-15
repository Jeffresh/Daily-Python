# Write your code inside the solve() function. In the first line print the name of the logical operation.
# If the logical operation is and or or, print hidden_operand in the second line.
# Your program shouldn't read any input or call the function, just implement it.

# def hidden_operation(operand):
#     if oper == "and":
#         return operand and hidden_operand
#     elif oper == "or":
#         return operand or hidden_operand
#     elif oper == "not":
#         return not operand

def solve():
    if hidden_operation('random_string') == 'random_string':
        print('or', hidden_operation(False), sep='\n')
    elif hidden_operation(False):
        print('not')
    else:
        print('and', hidden_operation(True), sep='\n')


if __name__ == '__main__':
    pass
