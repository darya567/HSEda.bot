from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



def get_categories():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Рестораны с средним чеком до 500руб')],
            [KeyboardButton(text='Рестораны с средним чеком от 500 до 1000руб')],
            [KeyboardButton(text='Рестораны с средним чеком от 1000руб')]
        ],
        resize_keyboard=True
    )
    return keyboard
