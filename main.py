from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
from aiogram import Router

bot = Bot('5473425325:AAE0NbhhR05q8VtrQ2Sa2QzwTyp6W31Flkc')
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Открыть Web App", web_app=WebAppInfo(url='https://твоя-ссылка-на-сайт'))]
        ],
        resize_keyboard=True
    )
    await message.answer('Запускаем Web App!', reply_markup=keyboard)

