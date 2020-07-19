# The list seconds is a list of numbers that represent seconds.
# Convert the number of seconds to full days and print
# the list that contains these values. The number of full days should be an int value.

if __name__ == '__main__':
    seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
    factor = 3600 * 24
    print([x // factor for x in seconds])
