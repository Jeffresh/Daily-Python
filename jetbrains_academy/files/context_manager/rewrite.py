# rewrite the folowing code using the with keyword:
#
# f = open('test.txt', 'w')
# f.write('Tada!')
# f.close()

# Please open a context manager with the name f


if __name__ == '__main__':
    with open('test.txt', 'w') as f:
        f.write('Tada!')
