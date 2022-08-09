import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

APP_KEY = 'w5lbt5pc42jrm20'
APP_SECRET = 'bhdxtu2vm0sqrgn'
# dbx = dropbox.Dropbox(App_key)

# dbx.users_get_current_account('Tavie Legasto')
# print(dbx)
Access_Code ='YLKC9hbw0rMAAAAAAAABOXNDmyAE8JpmL5wRSkaOArE'
# 'sl.BM9Du6d3B7TQJhFDFa3EW5rcJ3zxtSPEybwj754QFt6QM6g3BQG0JYAW7cI5CiJZZkZe4lAW1U6FJ2vkX7Wr2ghDPOm1GSmRH_a7obEUSk-Wc_5Ztdb-v6sn5vDHj84k8mQTbWo'
TOKKEN ='sl.BM_kqqAnIj1B6Fi3KXZEEOhjdq6k2mJWTWqmi_rkeB66HeaiFdaV5yZ8zrc7UsTo513gnwXSPJPM3O2jk8vSXfNlm2gKCEJ17Bmb4LWek8ETpBE2bFBfXVewHVam967gPqIpuUI'
# auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
dbx = dropbox.Dropbox(TOKKEN)


DEST = '/DTC/Parts/'
DEST = '/DTC/'
# dbx.files_create_folder(DEST +'main')
content =dbx.files_list_folder(DEST)
for i in content.entries:
	print(i.name)
# dbx.users_get_current_account()
# for entry in dbx.files_list_folder('').entries:
#     print(entry.name)
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