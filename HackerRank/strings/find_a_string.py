# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.
#
# NOTE: String letters are case-sensitive.


def count_substring(string, sub_string):
    n = len(string)
    n_sub = len(sub_string)
    substrings = [string[i:n_sub + i] for i in range(n - 2)]
    n_times = substrings.count(sub_string)

    return n_times


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
