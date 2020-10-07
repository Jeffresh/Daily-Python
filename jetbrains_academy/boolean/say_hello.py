# It's a common practice to say hello to users after they register on your website. In this task,
# you should implement a function that takes a string name as an argument and prints "Hello, NAME!"
# where NAME is replaced by the user's name. However, some users might want not to disclose their name so name can
# equal the empty string. In this case, your program should print "Hello, Anonymous!".
#
# Your program shouldn't read any input or call the function, just implement it.

def say_hello(name):
    print(f'Hello, {name}!') if name else print('Hello, Anonymous!')


if __name__ == '__main__':
    say_hello('')
    say_hello('Jeff')
