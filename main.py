from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# das

@dp.message_handler() # обработка сообшения и проверка по фильтру или условию
async def echo(message: types.Message):
    if message.text.count(" ") >= 1:
        await message.answer(text=message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dp)