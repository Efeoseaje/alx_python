"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    else:
        username = sys.argv[1]
        password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        r = response.json()
        print("{}".format(r.get("id")))
    else:
        print("None")
