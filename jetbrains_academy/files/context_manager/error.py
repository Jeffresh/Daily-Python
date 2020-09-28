# The code below is supposed to write years from 2010 to 2020 to the file years.txt However,
# something's wrong with the code.
#
# Find the mistake and fix it.

if __name__ == '__main__':
    with open('years.txt', 'w', encoding='utf-8') as f:
        for i in range(2010, 2020):
            f.write(str(i) + " ")
        f.write('2020')

    # f.write('2020')
