import os
import re
from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

done = False


@app.message(re.compile("(hey|hi|hello)"))
def wai_timer(message, say):
    try:
        say(f"Hey There <@{message['user']}>!")
    except:
        pass


@app.command('/rev')
def repeat_text(ack, say, command):
    try:
        ack()
        # channel_id = command["channel_id"]
        say(f"{command['text'][::-1]}")
    except:
        pass


@app.command('/echo')
def repeat_text(ack, say, command):
    try:
        ack()
        # channel_id = command["channel_id"]
        str_text = ''.join(command['text'])
        repeat = '! '.join([str_text] * 3) + '!'
        say(f"{repeat}")

    except:
        pass


# You probably want to use a database to store any conversations information ;)
conversations_store = {}


def fetch_conversations():
    try:
        # Call the conversations.list method using the WebClient
        result = app.client.conversations_list()
        save_conversations(result["channels"])

    except:
        pass
        # logger.error("Error fetching conversations: {}".format(e))


# Put conversations into the JavaScript object
def save_conversations(conversations):
    conversation_id = ""
    for conversation in conversations:
        # Key conversation info on its unique ID
        conversation_id = conversation["id"]

        # Store the entire conversation object
        # (you may not need all of the info)
        conversations_store[conversation_id] = conversation


fetch_conversations()
print(conversations_store)
