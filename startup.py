import app_config.app_config as app_config

from pathlib import Path

# def start_up_app() -> bool:

def start_app() -> bool:
    valid_update_id = app_config.setLastUpdateId()
    
    if not valid_update_id: return False

    return True
