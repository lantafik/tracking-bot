from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import config
import keyboards

bot = Bot(token=config.token)
dp = Dispatcher(bot)

class Form(StatesGroup):
    name = State()


@dp.message_handler(commands='start')
async def start(message: types.Message, state: FSMContext):
    await message.answer('Здравствуйте!\nВы попали в сервис отслеживания личного расписания!\nКак я могу к вам обращаться?')
    date = message.date
    await Form.name.set()

@dp.message_handler(state=Form.name)
async def set_name(message:types.Message, state: FSMContext):
    name = message.text
    await message.answer('Приятно познакомиться!...')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
