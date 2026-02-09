from __future__ import annotations
from dataclasses import dataclass

@dataclass
class TelegramUpdate:
    update_id: int | None
    message: TelegramMessage | None

@dataclass
class TelegramMessage:
    message_from: TelegramFrom | None
    date: int | None
    text: str | None

@dataclass
class TelegramFrom:
    first_name: str | None
    last_name: str | None