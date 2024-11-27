from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

register_role = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Student"), KeyboardButton(text='Teacher')]
    ]
)