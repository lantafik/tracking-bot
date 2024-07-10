from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from keyboards import *
import config
import keyboards
storage = MemoryStorage()

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/add - добавляет новую задачу
/delete - удаляет задачу
"""

bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    name = State()


@dp.message_handler(commands='start')
async def start(message: types.Message, state: FSMContext):
    await message.answer('Здравствуйте!\nВы попали в сервис отслеживания личного расписания!\nКак я могу к вам обращаться?')
    date = message.date
    await Form.name.set()

@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    name = message.text
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_menu, resize_keyboard=True)
    await message.answer(f'Приятно познакомиться, {name}!', reply_markup=keyboard)
    await state.finish()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)

@dp.message_handler(commands=['Начало и конец дня'])
async def time_changed(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_menu_start_and_end_day_2, resize_keyboard=True)
    await message.answer('Выберите действие:',reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
