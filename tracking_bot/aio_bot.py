from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

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
    await message.answer(f'Приятно познакомиться, {name}!')
    await state.finish()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

