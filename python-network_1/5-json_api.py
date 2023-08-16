""" Python script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
import sys


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) == 1:
        print('No result')
        sys.exit(1)
    else:
        payload = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        r = response.json()
        if r == {}:
            print('No result')
        else:
            print("[{}] {}".format(r.get('id'), r.get('name')))
    except ValueError:
        print("Not a valid JSON")
