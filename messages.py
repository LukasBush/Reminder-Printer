import app_config.app_config as app_config
import requests

def getMessages():
    new_messages = requests.get(
        url=f"{app_config.BASE_URL}/getUpdates",
        params={
            "offset": 0,
            "timeout": 30
        },
        timeout=35
    )

    print(new_messages.json())

#Filter out any messages that are /start