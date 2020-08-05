# A bunch of friends got together to watch an esports tournament. There are those who have already decided on
# their favorite team and those who are just interested in watching the competition.
#
# Write a function add_viewer() that will take a person's name and add it to the fan list if they already
# know which team they will root for. Return the list of all fans. If the person has not yet decided, then a
# new list should be created for them.
#
# If a person has their favorite team, then, together with the name of the person, a list containing names
# of all other fans will be passed as an argument to the function. If not, only the person's name will be given.
# Think about the default value for the list.
#
# You do NOT have to handle input or call a function, just implement it.


def add_viewer(name, team=None):
    if team is None:
        team = []
    team.append(name)
    return team


if __name__ == '__main__':
    print(add_viewer('Jeff'))
    print(add_viewer('John', ['Jeff']))
