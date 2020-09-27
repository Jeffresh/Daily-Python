# The file animals.txt has a list of animals, each written on a new line. For example:
#
# rabbit
# cat
# turtle
#
# Create a new file, animals_new.txt, where those animals are written on a single line and
# separated by whitespace.
#
# Don't forget to close the files!


if __name__ == '__main__':
    # read animals.txt
    animals = open('animals.txt', mode='r')
    # and write animals_new.txt
    animals_new = open('animals_new.txt', mode='a')

    for line in animals:
        animals_new.write(line.replace('\n', ' '))

    animals.close()
    animals_new.close()
