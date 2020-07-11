# You are given an HTML code snippet of N lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.
#
# Print the detected items in the following format:
#
# Tag1
# Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Tag3
# -> Attribute3[0] > Attribute_value3[0]
#

# Input Format
#
# The first line contains an integer N, the number of lines in the HTML code snippet.
# The next N lines contain HTML code.


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


if __name__ == '__main__':
    html = '\n'.join([input() for _ in range(int(input()))])
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
