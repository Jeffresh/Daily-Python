# Imagine that you are a hacker and you have got access to a web server
# written in Python. The problem is that it asks for a password that you do not know.
# However, this server is open source so you know that there is the wrong_password() function which takes
# a password and checks
# it against real_password.

real_password = "123"


def wrong_password(password):
    return (password == "" or (not password and real_password)) or password != real_password


def solve():
    print(wrong_password(False))


if __name__ == '__main__':
    solve()
