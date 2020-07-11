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
