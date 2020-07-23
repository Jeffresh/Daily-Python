# Morgan founded a company that sends satellites into the orbit to observe Earth from space. To headhunt the best
# aerospace engineers, Morgan decided to pay a welcome bonus equal to 35% of the base salary. However, the bonus may
# be even higher for a particular candidate.
#
# Declare a function get_bonus() below that would calculate this bonus. It should take two arguments, salary and
# percentage, with a default value 35 for the last one. Return only the integer part of the bonus.


from math import floor


def get_bonus(salary, percentage=35):
    return floor(salary * percentage / 100)


if __name__ == '__main__':
    print(get_bonus(13000, 39))
