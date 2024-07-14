import requests
import json

class Slack:
    def __init__(self, webhook_url, channel):
        self.webhook_url = webhook_url
        self.channel = channel
    
    def send_message(self, message):
        headers = {'Content-Type': 'application/json'}
        data = {
            'channel': self.channel,
            'text': message
        }
        response = requests.post(self.webhook_url, headers=headers, data=json.dumps(data))
        
        return response.status_code


webhook_url = ''
channel = '#test'
co_Likha = Slack(webhook_url, channel)


message = 'test message using python'
co_Likha.send_message(message)
