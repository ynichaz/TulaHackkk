from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
inline_btn_1 = InlineKeyboardButton(text='админ', callback_data='button1')
inline_btn_2 = InlineKeyboardButton(text='пользователь', callback_data='button2')

inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2)

btn1 = InlineKeyboardButton(text='создать новый опрос', callback_data='btn1')
admin1 = InlineKeyboardMarkup(row_width=2).add(btn1)

# клава с новым вопросом
vopr1 = InlineKeyboardButton(text='создать новый вопрос', callback_data='input_text')
vopr3 = InlineKeyboardButton(text='посмотреть все созданные вопросы', callback_data='vopr3')
vopr2 = InlineKeyboardButton(text='визулизация опроса', callback_data='vopr2', web_app=WebAppInfo(url='http://127.0.0.1:5000'))
vopr = InlineKeyboardMarkup(row_width=1).add(vopr1, vopr3, vopr2)

# vopr1 = KeyboardButton('создать новый вопрос')
# vopr2 = KeyboardButton('посмотреть все созданные вопросы')
# vopr3 = KeyboardButton('визулизация опроса')
#
# vopr_keyboard = ReplyKeyboardMarkup(row_width=1)
# vopr_keyboard.add(vopr1, vopr2, vopr3)

#клава с вопросами текущего опроса
nazad = InlineKeyboardButton(text='назад', callback_data='back')
voprfull = InlineKeyboardMarkup(row_width=1).add(nazad)
