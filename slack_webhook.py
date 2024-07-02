import requests
import json

class coLinkha:
    def __init__(i, webhook_url, channel):
        i.webhook_url = webhook_url
        i.channel = channel
    
    def send_message(i, message):
        headers = {'Content-Type': 'application/json'}
        data = {
            'channel': i.channel,
            'text': message
        }
        response = requests.post(i.webhook_url, headers=headers, data=json.dumps(data))
        
        print(response.status_code)


webhook_url = ''
channel = '#test'
co_Likha = coLinkha(webhook_url, channel)


message = 'test message using python'
co_Likha.send_message(message)
