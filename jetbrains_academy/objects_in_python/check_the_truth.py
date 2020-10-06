# Write a function check_values that accepts two values (for example, 0 , 1 or 'string' and []) and checks if both
# of them are True. To achieve this, convert hte values via the built-in bool() function.

# If both values are True, the your function should return True, otherwise False. Note that you are NOT supposed
# to call teh function, just implement it.

def check_values(first_value, second_value):
    return bool(first_value) and bool(second_value)


if __name__ == '__main__':
    print(check_values(0, 'string'))
