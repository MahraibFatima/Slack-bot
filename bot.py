import slack
import os
from pathlib import Path
from dotenv import load_dotenv

env_path= Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN_'])

def send_message(message):
    client.chat_postMessage(channel='#test', text=message)


if __name__ == "__main__": 
    send_message('Hello World!')