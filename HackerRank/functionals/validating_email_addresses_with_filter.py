def fun(s):
    name, dom = s.split('@') if len(s.split('@')) == 2 else ('*', '*')
    web, extension = dom.split('.') if '.' in dom else ('*', '*')
    return web.isalnum() and 0 < len(extension) < 4 and all(
        map(lambda x: x.isalnum() or x == '-' or x == '_', name)) and name


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
