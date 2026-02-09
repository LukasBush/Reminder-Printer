from .models import TelegramUpdate, TelegramFrom, TelegramMessage

def parse_update(data: dict) -> TelegramUpdate:
    final_message = None
    received_message = data.get("message")
    if received_message:
        from_user = received_message.get("from")
        final_message = TelegramMessage(
            date = received_message.get("date"),
            text = received_message.get("text"),
            message_from = TelegramFrom(
                first_name = from_user.get("first_name"),
                last_name = from_user.get("last_name")
            ),
        )

    return TelegramUpdate(
        update_id = data.get("update_id"),
        message = final_message
    )