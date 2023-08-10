""" This script fetches a request from a url"""


import requests

req = requests.get("https://alu-intranet.hbtn.io/status")
print(req)