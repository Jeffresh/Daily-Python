# From the input, you get the first and the last name of a person. Create a tuple with the full name:
# the first element should be the first name and the second element should be the last name.
# Save the resulting tuple to the variable full_name. Do NOT print anything!
#
# The variables first_name and last_name have already been read from input.
#
# Example. Suppose, first_name is "John" and last_name is "Doe". The resulting tuple should be ("John", "Doe")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    full_name = (first_name, last_name)
