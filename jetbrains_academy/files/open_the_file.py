# Create a file "stars.txt" and open it for writing as text in the UTF-16 encoding. Name the variable
# test_file. Don't forget to clos the file!


if __name__ == '__main__':
    test_file = open('stars.txt', mode='w', encoding='utf-16')
    test_file.close()