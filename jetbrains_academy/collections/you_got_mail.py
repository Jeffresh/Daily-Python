# Email addresses usually have the same structure: someone@somewhere.com (or any other domain).
#
# You are working with a database of email addresses from an imaginary email service yougotmail.com.
# Create a program that would separate the local-part that precedes the @ sign from the rest of the address.
#
# The input format:
#
# The email address. It is stored in the variable email, you do not need to work directly with input.
#
# The output format:
#
# The local-part of the address.


if __name__ == '__main__':
    # write your code here
    # remember: the variable email is already defined

    email = "john.andrew.smith@yougotmail.com"

    name = email.split('@')[0]
    print(name)
