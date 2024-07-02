import aiogram

from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = '7250507637:AAHhLqUtN0EZWz9Nd0ojpywHrfZ5FrRWW6A'

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer(text="Добро пожаловать в мой телеграмм бот!")
    await message.delete()
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)


if __name__ == "__main__":
    executor.start_polling(dp)

