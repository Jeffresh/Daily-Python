# Task
# When users post an update on social media,such as a URL, image, status update etc.
# , other users in their network are able to view this new post on their news feed.
# Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
#
# Since sometimes posts are published and viewed in different time zones, this can be confusing.
# You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
#
# Day dd Mon yyyy hh:mm:ss +xxxx
#
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.


# Input Format
#
# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t1 and time t2 .

from datetime import datetime

if __name__ == '__main__':
    test_cases = int(input())
    fmt = '%a %d %b %Y %H:%M:%S %z'

    for _ in range(test_cases):
        t1 = input()
        t2 = input()
        seconds = (datetime.strptime(t1, fmt) - datetime.strptime(t2, fmt)).total_seconds()
        print("{:.0f}".format(abs(seconds)))
