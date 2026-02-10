import config
import telegram.parser as parser
import requests
import state.offset_store as state

from telegram.models import TelegramUpdate
from typing import List

#TRY TO MAKE IT SO THIS SIMPLY GETS THE MESSAGES, ALL OTHER WORK IS IN OTHER FUNCTIONS
def getMessages() -> List[TelegramUpdate]:
    received_messages = requests.get(
        url=f"{config.BASE_URL}/getUpdates",
        params={
            "offset": config.GLOBAL_OFFSET,
            "timeout": 30
        },
        timeout=35
    )

    message_data = received_messages.json()
    new_messages = message_data.get("result", [])

    if not new_messages:
        return []

    final_messages = []
    for message in new_messages:
        parsed_message = parser.parse_update(message)
        final_messages.append(parsed_message)

    return final_messages