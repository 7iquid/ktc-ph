import requests
import json

# url = 'http://127.0.0.1:8000/Accounts/register'
url = 'https://ktc-ph-api.herokuapp.com/api/'
# Headers ={
#     "Authorization": "Basic dzVsYnQ1cGM0MmpybTIwOmJoZHh0dTJ2bTBzcXJnbg== ",
#     "Content-Type": "application/json"
# }


# Data = {
#     "oauth1_token":"sl.BNdWsTb3MBxnwtwQgHQ1Hgi4SO6X14DbBzm9KgULUh81SBXhGXD7mxKWqUDDqDoKmd65IeHXPG-FNNcbBZpDvEUTYLZOiGHA8-nz1L8tL5lVJqaQ0Z5gFID5MHqnPbZBekBiMKYuNP-y",
#     "oauth1_token_secret":"bhdxtu2vm0sqrgn"
# }

response = requests.get(url )
# data = response.json()
print(json.dumps(response.json(), indent=2))

