from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TelegramUpdate:
    update_id: int
    message: TelegramMessage

@dataclass
class TelegramMessage:
    message_from: TelegramFrom
    date: int | None
    text: str

@dataclass
class TelegramFrom:
    first_name: str
    last_name: str