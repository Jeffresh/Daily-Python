# Task
#
# You are given an HTML code snippet of
#
# lines.
# Your task is to print start tags, end tags and empty tags separately.
#
# Format your results in the following way:
#
# Start : Tag1
# End   : Tag1
# Start : Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Start : Tag3
# -> Attribute3[0] > None
# Empty : Tag4
# -> Attribute4[0] > Attribute_value4[0]
# End   : Tag3
# End   : Tag2
#

# Input Format
#
# The first line contains integer N, the number of lines in a HTML code snippet.
# The next N lines contain HTML code.


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            [print('->', attr, '>', val) for attr, val, in attrs]

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)


if __name__ == '__main__':
    line_number = int(input())
    my_parser = MyHTMLParser()
    ss = '\n'.join([input() for x in range(line_number)])
    my_parser.feed(ss)
