import state.offset_store as offset_store

def start_app() -> bool:
    valid_update_id = offset_store.getLastUpdateId()
    
    print(valid_update_id)

    if valid_update_id < 0: 
        return False

    if not offset_store.setLastUpdateId(valid_update_id + 1):
        return False

    return True