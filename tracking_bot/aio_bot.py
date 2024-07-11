from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import numpy as np

from keyboards import *
import config
from connect import *
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

class DataCollectionForm(StatesGroup):
    id = State()  # Ожидание ID
    name = State()  # Ожидание имени
    date_reg = State()  # Ожидание даты регистрации
    day_start = State()  # Ожидание начала дня
    day_end = State()  # Ожидание конца дня


@dp.message_handler(commands='start')
async def start(message: types.Message, state: FSMContext):
    await message.answer('Здравствуйте!\nВы попали в сервис отслеживания личного расписания!\nКак я могу к вам обращаться?')
    date = message.date
    await Form.name.set()

@dp.message_handler(state=Form.name)
async def set_name(message: types.Message, state: FSMContext):
    name = message.text
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_ak, resize_keyboard=True)
    await message.answer(f'Приятно познакомиться, {name}!', reply_markup=keyboard)
    await state.finish()

@dp.message_handler(commands=['register'])
async def reg(message: types.Message, state: FSMContext):
    await DataCollectionForm.id.set()
    await message.answer("придумайте свой id")

@dp.message_handler(state=DataCollectionForm.id)
async def set_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await DataCollectionForm.name.set()
    await message.answer("введите своё имя")

@dp.message_handler(state=DataCollectionForm.name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await DataCollectionForm.date_reg.set()
    await message.answer("введите дату регистрацции(2022-08-08)")

@dp.message_handler(state=DataCollectionForm.date_reg)
async def set_date_reg(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date_reg'] = message.text
    await DataCollectionForm.day_start.set()
    await message.answer("введите время начала дня(8:00)")

@dp.message_handler(state=DataCollectionForm.day_start)
async def set_day_start(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['day_start'] = message.text
    await DataCollectionForm.day_end.set()
    await message.answer("введите время конца дня(22:00)")

@dp.message_handler(state=DataCollectionForm.day_end)
async def set_day_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['day_end'] = message.text
        id = data.get('id')  # Получаем сохраненное ID
        name = data.get('name')  # Получаем сохраненное имя
        date_reg = data.get('date_reg')
        day_start = data.get('day_start')
        day_end = data.get('day_end')
        add_new_user(id, name, date_reg, day_start, day_end)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)

@dp.message_handler(commands=['day_settings'])
async def time_changed(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_menu_start_and_end_day_2, resize_keyboard=True)
    await message.answer('Выберите действие:',reply_markup=keyboard)

@dp.message_handler(commands=['Change_the_start_of_the_day'])
async def time_changed(message: types.Message):
    await message.answer(f'меняем время')

@dp.message_handler(commands=['List_of_codes'])
async def time_changed(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_menu_change_codes, resize_keyboard=True)
    await message.answer('Выберите действие:', reply_markup=keyboard)
@dp.message_handler(commands=['Schedule_history'])
async def time_changed(message: types.Message):
    await message.answer(f'история')

@dp.message_handler(commands=['Start_of_the_schedule'])
async def time_changed(message: types.Message):
    await message.answer(f'расписание')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
