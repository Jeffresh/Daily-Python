# Your friend started writing an algorithm that takes a list of names and counts the number of names starting with
# a capital letter. Your friend is still learning Python and doesn't know how to complete this algorithm.
# Help your friend finish the implementation. You only need to finish the algorithm function,
# you do NOT need to work with the input data!
#
# Don't forget to think about corner cases!

def startswith_capital_counter(names):
    with_capital = 0
    for name in names:
        with_capital += 1 if name.istitle() else 0
    return with_capital


if __name__ == '__main__':
    print(startswith_capital_counter(['Zaramay', 'Duko', 'Mesita', 'cavergas']))
