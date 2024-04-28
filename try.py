from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='7128799686:AAEScq_JGe94JSaLgw4VbYnC11TKIA7COAQ')
dp = Dispatcher(bot, storage=MemoryStorage())

class InputText(StatesGroup):
    waiting_for_text = State()

@dp.message_handler(Command('start'))
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Ввести вопрос', callback_data='input_text')
    keyboard.add(button)
    await message.answer('Welcome! Click the button below to input text.', reply_markup=keyboard)

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

if __name__ == '__main__':
    executor.start_polling(dp)