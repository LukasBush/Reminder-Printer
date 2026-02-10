import config
import state.offset_store as offset_store

def start_app() -> bool:
    valid_update_id = offset_store.getLastUpdateId()

    if valid_update_id < 0: 
        return False
    
    config.GLOBAL_OFFSET = valid_update_id

    return True