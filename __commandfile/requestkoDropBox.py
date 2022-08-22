import requests
import json

url = 'https://api.dropboxapi.com/2/auth/token/from_oauth1'

Headers ={
    "Authorization": "Basic dzVsYnQ1cGM0MmpybTIwOmJoZHh0dTJ2bTBzcXJnbg== ",
    "Content-Type": "application/json"
}


Data = {
    "oauth1_token":"sl.BNdWsTb3MBxnwtwQgHQ1Hgi4SO6X14DbBzm9KgULUh81SBXhGXD7mxKWqUDDqDoKmd65IeHXPG-FNNcbBZpDvEUTYLZOiGHA8-nz1L8tL5lVJqaQ0Z5gFID5MHqnPbZBekBiMKYuNP-y",
    "oauth1_token_secret":"bhdxtu2vm0sqrgn"
}

response = requests.post(url ,headers=Headers, data=json.dumps(Data))
print(response)

