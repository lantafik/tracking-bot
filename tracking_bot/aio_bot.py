from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import numpy as np
import pandas as pd
import os
import openpyxl
from datetime import datetime
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
    await message.answer(
        'Здравствуйте!\nВы попали в сервис отслеживания личного расписания!\nКак я могу к вам обращаться?')
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
    async with state.proxy() as data:
        data['date_reg'] = message.date
    await DataCollectionForm.name.set()
    await message.answer("введите своё имя")


@dp.message_handler(state=DataCollectionForm.name)
async def set_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['name'] = message.text
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
    await message.answer('Выберите действие:', reply_markup=keyboard)


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


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def process_document(message: types.Message):
    FILE_FOLDER = r'C:\Users\User\Desktop\бот'
    file_id = message.document.file_id
    document = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(document.file_path)

    data = downloaded_file.getvalue()

    save_path = os.path.join(FILE_FOLDER, message.document.file_name)
    with open(save_path, 'wb') as new_file:
        new_file.write(data)

    # Открываем скачанный файл Excel
    wb = openpyxl.load_workbook(save_path)
    ws = wb.active

    # Преобразуем данные из Excel в DataFrame для удобства работы
    df = pd.DataFrame(ws.values)

    # Добавляем три новые колонки с названиями 'NewColumn1', 'NewColumn2', 'NewColumn3'
    new_columns = ['NewColumn1', 'NewColumn2', 'NewColumn3']
    for column_name in new_columns:
        df[column_name] = 0

    # Сохраняем измененный DataFrame обратно в Excel
    output_filename = f"processed_{message.document.file_name}"
    df.to_excel(os.path.join(FILE_FOLDER, output_filename), index=False)

    # Закрываем книгу
    wb.close()

    # Отправляем отредактированный файл обратно
    await bot.send_document(chat_id=message.chat.id, document=open(os.path.join(FILE_FOLDER, output_filename), 'rb'))

    await message.reply("Файл обработан.")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

