import textwrap


def wrap(string, max_width):

    string_size = len(string)
    reminder = string_size % max_width
    wrapped = [string[i*max_width:(i+1)*max_width]
               for i in range(string_size//max_width)]

    if reminder != 0:
        wrapped = wrapped + [string[string_size - reminder:]]

    wrapped = '\n'.join(wrapped)

    return wrapped


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
