#!/usr/bin/env python3

import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
import requests
'''
This example walks through a basic oauth flow using the existing long-lived token type
Populate your app key and app secret in order to run this locally
'''
APP_KEY = "w5lbt5pc42jrm20"
APP_SECRET = "bhdxtu2vm0sqrgn"
AUTHORIZATION_CODE = '7Trh4gb4k8MAAAAAAAAAAbCxLpgIvuq4rzIQKjX2fLDewbJCmCxsCuMLHSdobM7_'
# auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

# authorize_url = auth_flow.start()
# print("1. Go to: " + authorize_url)
# print("2. Click \"Allow\" (you might have to log in first).")
# print("3. Copy the authorization code.")
# auth_code = input("Enter the authorization code here: ").strip()

# try:
#     oauth_result = auth_flow.finish(auth_code)
# except Exception as e:
#     print('Error: %s' % (e,))
#     exit(1)

# with dropbox.Dropbox(oauth2_access_token=oauth_result.access_token) as dbx:
#     dbx.users_get_current_account()
#     print("Successfully set up client!")

# # curl -u APP_KEY:APP_SECRET \
# -d "code=AUTHORIZATION_CODE&grant_type=authorization_code" \
# -H "Content-Type: application/x-www-form-urlencoded" \
# -X POST "https://api.dropboxapi.com/oauth2/token"
# import requests

# r = requests.get('https://github.com/timeline.json')
# r.json()
url = 'https://api.dropboxapi.com/oauth2/token'

data = {
    'code': AUTHORIZATION_CODE,
    'grant_type': 'authorization_code',
}

response = requests.post(url, data=data, auth=(APP_KEY , APP_SECRET))
print(response.json())