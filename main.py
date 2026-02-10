import config
import startup
import processing.validator as validate
import time
from operator import attrgetter
import telegram.api as messages
import state.offset_store as state

def main():
    if not startup.start_app():
        print("Error in start up")
        return
    
    while not config.SHUT_DOWN:
        #If you want a delay between polling
        time.sleep(6000)
        #Grab messages
        received_messages = messages.getMessages()
        if not received_messages: continue
        #Set the new offset
        newest_message = max(received_messages, key=attrgetter("update_id"))
        state.setLastUpdateId(newest_message.update_id)
        #Validate messages
        viable_messages = validate.validateMessages(received_messages)
        if not viable_messages: continue
        #Send to printer
        #USE A FOR LOOP?
        
        print(viable_messages)

if __name__ == "__main__":
    main()