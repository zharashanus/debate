import requests
from openai_api_token import *
import base64
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

# Предполагаем, что client_id и client_secret уже определены
client_id = auth_data
client_secret = client_secret
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

payload = 'scope=GIGACHAT_API_PERS'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': '123124',
  'Authorization': f'Basic {encoded_credentials}'
}

response = requests.post(url, headers=headers, data=payload, verify=False)

print(response)