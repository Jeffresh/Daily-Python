# Write a program that calculates how many unique letters the input word has.
# The word is stored in the variable word. Print out the result you'll get.

if __name__ == '__main__':
    word = input()  # the input word
    print(len(set(word)))