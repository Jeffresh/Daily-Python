# Given a list of words in the code below, create a list of lengths of those words and print it.

if __name__ == '__main__':
    words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
             "apothecary"]

    lens = [len(word) for word in words]

    print(lens)
