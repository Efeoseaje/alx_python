""" This script fetches a request from a url and
displays the value of the variable X-Request-Id
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    # print(response.headers['X-Request-Id'])
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print("{}".format(x_request_id))
    else:
        print("X-Request-Id header not found in the response.")
