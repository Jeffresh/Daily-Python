# Several warm-up matches have been played at the tennis tournament.
# You have data on the victories and losses of some players. Save the names of
# the winners to a list and calculate the total number of victories.

# The input format:
#
# On the first line, you'll receive the integer n specifying a number of lines.
#
# The next n lines will look like either Name win or Name loss.
#
# The output format:
#
# On the first line, print out the list of all players that have won a match,
# repeat the names if necessary.
#
# Then output the total number of victories based on your list.

if __name__ == '__main__':
    n = int(input())
    winners = [i[0] for i in [input().split() for _i in range(n)] if i[1] == 'win']
    print(winners, len(winners), sep='\n')
