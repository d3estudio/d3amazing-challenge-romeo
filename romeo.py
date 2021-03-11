from interactive_romeo import chat
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_TOKEN'], '/slack/events', app)

client = slack.WebClient(os.environ['BOT_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

chat = chat.conversation_romeo()

@slack_event_adapter.on('message')

def message(payLoad):

    event = payLoad.get('event',{})
    user_id = event.get('user')

    if BOT_ID != user_id:

        text = event.get('text')

        answer = chat.answer(user_id, text)
        
        client.chat_postMessage(channel=user_id,text=answer)
        

if __name__ == "__main__":
    app.run(debug=True)
