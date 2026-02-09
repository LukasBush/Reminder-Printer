import config
from pathlib import Path

LAST_UPDATE_FILE = Path(__file__).parent / "last_update_id.txt"

def getLastUpdateId() -> int:
    last_update_file = Path(LAST_UPDATE_FILE)
    try:
        file_content = last_update_file.read_text(encoding = "utf-8").strip()
        if file_content:
            return int(file_content)
        else:
            return -1
    except:
        return -1


def setLastUpdateId(update_id: int) -> bool:
    try:
        file_path = Path(LAST_UPDATE_FILE)
        temp_file = file_path.with_suffix(".tmp")
        temp_file.write_text(str(update_id), encoding = "utf-8")
        temp_file.replace(file_path)
        config.GLOBAL_OFFSET = update_id
        return True
    except:
        return False
