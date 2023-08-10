""" This script fetches a request from a url"""


import requests

response = requests.get("https://alu-intranet.hbtn.io/status")
response_url = response.url
response_text = response.text

print('Body response:')
print('\t- type: {}'.format(type(response_url)))
print('\t- content: {}'.format(response_text))
