# Declare a function called create_url(). It should take two arguments host and port and return URL in the format "https://{host}:{port}".
#
# Set default values for both parameters: a string "localhost" and an integer 443 respectively. Called without arguments,
# the function would return "https://localhost:443".


def create_url(host='localhost', port=443):
    return 'https://{}:{}'.format(host, port)


if __name__ == '__main__':
    print(create_url('nasa.gov'))
