# How many asterisk(*) will you see after the program is executed?

if __name__ == '__main__':
    i = 0
    while i < 5:
        print('*')  # 4 asterisks
        if i % 2 == 0:
            print('**')  # 2 pairs of two asterisks = 4 asterisks
        if i > 2:
            print('***')  # 3 paris of 3 asterisks  = 9 asterisks
        i = i + 1

# 4 + 4 + 9 = 17 asterisks
