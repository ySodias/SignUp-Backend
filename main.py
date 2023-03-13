from flask import Flask

import requests

app = Flask(__name__)

url = "https://login.microsoftonline.com/common/oauth2/token"

payload='grant_type=password&scope=openid&resource=https%3A%2F%2Fanalysis.windows.net%2Fpowerbi%2Fapi&client_id=b142d4c6-0f74-4114-87db-875079893e26&username=r&password='

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'fpc=Ar9JAx08weZOsOREf4rEufI_8lkqAQAAAJws5NkOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
}

@app.route('/token')
def get_token():
    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['access_token']

if __name__=='__main__':
    app.run()

