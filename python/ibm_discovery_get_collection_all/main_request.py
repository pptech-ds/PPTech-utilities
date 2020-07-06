import requests

# Define API constant parameters
API_URI = 'https://gateway.watsonplatform.net/discovery/api'
API_USR = 'raphael.moraglia.@PPTECH.com'
API_KEY = 'WOMqeAx8wH8S-0CX6Nzn3B_4AC8hyqwEz8KbgPgii4jA'

# First authenticate with user
# res = requests.post(API_URI + '/auth/token', json={'email': API_USR, 'password': API_PWD})
res = requests.get(API_URI, auth=(API_KEY))

# Ensure user is authenticated
if res.status_code != 200:
    print('Error, not connected')
    exit(1)
