""" This script fetches a request from a url and
displays the value of the variable X-Request-Id
"""


# import requests
# import sys
# 
# if __name__ == "__main__":
    # url = sys.argv[1]
    # response = requests.get(url)
    # # print(response.headers['X-Request-Id'])
    # x_request_id = response.headers.get('X-Request-Id')
    # if x_request_id:
        # print("{}".format(x_request_id))
    # else:
        # print("X-Request-Id header not found in the response.")

import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        return

    url = sys.argv[1]
    
    try:
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(f"{x_request_id}")
        else:
            print("X-Request-Id header not found in the response.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

if __name__ == "__main__":
    main()
