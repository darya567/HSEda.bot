from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def get_categories():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Рестораны со средним чеком до 500 р.')],
            [KeyboardButton(text='Рестораны со средним чеком от 500 до 1000 р.')],
            [KeyboardButton(text='Рестораны со средним чеком от 1000 р.')]
        ],
        resize_keyboard=True
    )
    return keyboard
