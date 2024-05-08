from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import get_kb_text


def get_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text=get_kb_text().weather_by_geo, request_location=True))
    builder.row(KeyboardButton(text=get_kb_text().weather_by_city))
    return builder.as_markup(resize_keyboard=True)