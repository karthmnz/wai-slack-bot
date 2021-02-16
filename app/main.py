import os
import re
from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

done = False
@app.message(re.compile("(hey|hi|hello|Hey|Hi|Hello)"))
def wai_timer(message, say):
    say(f"Hey There <@{message['user']}>!")
        


@app.command('/rev')
def repeat_text(ack, say, command):
    ack()
    # channel_id = command["channel_id"]
    say(f"{command['text'][::-1]}")


@app.command('/echo')
def repeat_text(ack, say, command):
    ack()
    #channel_id = command["channel_id"]
    str_text = ''.join(command['text'])
    repeat = '! '.join([str_text] * 3) + '!'
    say(f"{repeat}")
