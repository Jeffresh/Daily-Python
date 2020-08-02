# The string below has an encoded message. To find out what it is, take every 5th letter starting
# from the first one, and then reverse the sequence. Spaces are considered as symbols here.
# Don't forget to print what you've got!

if __name__ == '__main__':
    string = "no clouds here to spy on pets"
    decode = string[::5][::-1]
    print(decode)
