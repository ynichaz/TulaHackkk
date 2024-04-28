from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery
from aiogram.types.web_app_info import WebAppInfo
from pyvis.network import Network
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import keyboard as kb
import keyboard as nav
import sqlite3

net = Network()

class InputText(StatesGroup):
    waiting_for_text = State()

API_TOKEN = '7128799686:AAEScq_JGe94JSaLgw4VbYnC11TKIA7COAQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, выбери свою роль',
                           reply_markup=kb.inline_kb_full)

@dp.callback_query_handler()
async def send_message(call: types.CallbackQuery):
    if call.data == 'button1':
        user_id = call.from_user.id
        with sqlite3.connect('/Users/varya_kurkubet/Desktop/database.db') as db:
            cursor = db.cursor()
            info = cursor.execute('SELECT * FROM admins WHERE username=?', (user_id,)).fetchone()

            if info is None:
                await bot.send_message(call.from_user.id, 'вы не админ')
            else:
                await bot.send_message(call.from_user.id, 'проверка на админа пройдена, вам выданы права администратора',
                                       reply_markup=kb.admin1)
        db.close()

    if call.data == 'btn1':
        # await bot.send_message(call.from_user.id, 'выберите действие', reply_markup=nav.vopr_keyboard)
        await call.message.edit_reply_markup(kb.vopr)


@dp.callback_query_handler(lambda c: c.data == 'input_text')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await InputText.waiting_for_text.set()
    await callback_query.message.reply('Введите вопрос')

@dp.message_handler(state=InputText.waiting_for_text)
async def process_text(message: types.Message, state: StatesGroup):
    await state.finish()
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text=message.text, callback_data=message.text)
    keyboard.add(button)
    await message.reply('ваш вопрос сохранен', reply_markup=keyboard)

    # if call.data == 'vopr1':
    #     net.add_node(1, label=message.text)
    #     addvopr = InlineKeyboardButton(text=message.text, callback_data='1')
    #     kb.voprfull.add(addvopr)
    #     await call.message.edit_reply_markup(kb.voprfull)
    #
    # if call.data == 'vopr3':
    #     await call.message.edit_reply_markup(kb.voprfull)




# @dp.message_handler()
# async def bot_message(message: types.Message):
#     if message.text == 'создать новый вопрос':
#         await bot.send_message(message.from_user.id, 'введите текст вопроса')
#     #
#     # if message.text == 'введите текст вопроса':
#         await answers.step1.set()
#         a = message.text
#         net.add_node(1, label=a)
#         addvopr = InlineKeyboardButton(text=a, callback_data='1')
#         kb.voprfull.add(addvopr)
#         await bot.send_message(message.from_user.id, 'успешно'+ str(answers.step1), reply_markup=nav.vopr_keyboard)
#
#     if message.text == 'посмотреть все созданные вопросы':
#         await bot.send_message(message.from_user.id, 'список ваших вопросов', reply_markup=kb.voprfull)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

