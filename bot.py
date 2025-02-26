import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, Response, request
from slackeventsapi import SlackEventAdapter

env_path= Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__) 
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET_'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN_'])
BOT_ID = client.api_call("auth.test")['user_id']

message_counts= {}
welcome_messages = {}

class WelcomeMessage:
    START_TEXT = {
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': (
                'Welcome to this channel! \n\n'
                '*Get started by completing the tasks!*'
            )
        }
    }
    DIVIDER = {'type': 'divider'}

    def __init__(self, channel, user):
        self.channel = channel
        self.user = user
        self.icon_emoji = ':robot_face:'
        self.timestamp = ''
        self.completed = False
        #self.text = f"Welcome to the channel <@{user}>! We are glad to have you here!"
    
    def get_message_payload(self):
        return {
            'ts': self.timestamp,
            'channel': self.channel,
            'username': 'Welcome Robot!',
            'icon_emoji': self.icon_emoji,
            'blocks': [
                self.START_TEXT,
                self.DIVIDER,
                *self._get_reaction_task()
            ]
        }
    
    def _t_reaction_task(self): 
        checkmark = ':white_check_mark:'
        if not self.completed:
            checkmark = ':white_large_square:'
        text = f"{checkmark} *React to this message!*"  
        return [{'type': 'section', 'text': {'type': 'mrkdwn', 'text': text}}]

def send_welcome_message(channel, user):
    welcome = WelcomeMessage(channel, user)
    message = welcome.get_message_payload()
    response = client.chat_postMessage(**message) 
    welcome.timestamp = response['ts']

    if channel not in welcome_messages:
        welcome_messages[channel] = {}
    welcome_messages[channel][user] = welcome
    #client.chat_postMessage(channel='#test', text=message)

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if BOT_ID != user_id and user_id != None:
        if user_id in message_counts:
            message_counts[user_id] += 1
        else:
            message_counts[user_id] = 1
        if text.lower() == 'start':
            send_welcome_message(f'@{user_id}', user_id)
            # welcome = WelcomeMessage(channel_id, user_id)
            # client.chat_postMessage(**welcome.get_message_payload())
        #send_message(text)

@app.route('/message-count', methods=['GET', 'POST'])
def message_count():
    data= request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    message_count = message_counts.get(user_id, 0)
    client.chat_postMessage(channel=channel_id, text=f"Message: {message_count}")
    return Response(), 200

if __name__ == "__main__": 
    app.run(debug=True)
    #message('Hello World!')
    #send_message('Hello World!')
    