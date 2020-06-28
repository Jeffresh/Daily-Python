# Task
# You are given three integers: a, b and m , respectively. Print two lines.
# The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

if __name__ == '__main__':
    base = int(input())
    power = int(input())
    mod = int(input())

    pow_value = pow(base, power)
    pow_mod_value = pow(base, power, mod)

    print(pow_value)
    print(pow_mod_value)
