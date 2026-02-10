import config
import re
from typing import List
from telegram.models import TelegramUpdate

ALPHANUMERIC_REGEX = re.compile(r"^[A-Za-z0-9 ]+$")

def validateMessages(messages: List[TelegramUpdate]) -> List[TelegramUpdate]:
    stop_flag = False
    filtered_messages = []
    for message in messages:
        text = message.message.text.strip()

        #Check for shutdown command
        if (not stop_flag 
            and text == "/shutdown" 
            and message.message.message_from.first_name == "Lukas" 
            and message.message.message_from.last_name == "Bush"
        ):
           config.SHUT_DOWN = True
           stop_flag = True 
           continue

        #Filter out start command messages
        if text == "/start":
            continue

        #Only allowing regex for now
        if not ALPHANUMERIC_REGEX.match(text):
            continue

        filtered_messages.append(message)


    return filtered_messages
