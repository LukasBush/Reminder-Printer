from pathlib import Path

BOT_TOKEN = "8319148720:AAEB291OrCn6cWEs_E9ITBupf9avIwUPcEk"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
GLOBAL_OFFSET = -1
LAST_UPDATE_FILE = Path(__file__).parent / "last_update_id.txt"

def getLastUpdateId() -> bool:
    last_update_file = Path(LAST_UPDATE_FILE)
    try:
        file_content = last_update_file.read_text(encoding = "utf-8").strip()
        if file_content:
            GLOBAL_OFFSET = int(file_content)
            return True
        else:
            return False
    except:
        return False


def setLastUpdateId() -> bool:
    return True