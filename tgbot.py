import requests
token = '6565535139:AAHNbWTCvVozktkxFE6g1F4_TBX22ttFtaY'
main_url = f'https://api.telegram.org/bot{token}'
#url = f'{main_url}/getMe'

result = requests.get(url)
print(result.json())

url = f'{main_url}/getUpdates'
#result = requests.get(url)
#pprint.pprint(result.json())
messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Привет дорогой пользыватель!'
    }
    result = requests.post(url,params=params)