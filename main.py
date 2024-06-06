import asyncio

from aiogram.methods.delete_webhook import DeleteWebhook
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, Filter
from aiogram.fsm.context import FSMContext
from config import TOKEN_BOT, ID
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


router = Router()
bot = Bot(TOKEN_BOT)
dp = Dispatcher()

async def main():  
    dp.include_router(router)

    await bot.delete_webhook()
    #await dp.start_polling(bot, polling_timeout=30000, close_bot_session=True)
    main = InlineKeyboardMarkup(inline_keyboard=
                            [
                                [InlineKeyboardButton(text='Фундамент для новичков 👉', url="google.com")],
                                [InlineKeyboardButton(text='Оставить отзыв', url="https://t.me/ru2ch")],
                                [InlineKeyboardButton(text='Предложения по улучшению клуба 🔥', url="https://t.me/psyriotyk")],
                                [InlineKeyboardButton(text='Предложения по сотрудничеству 🔥', url="https://t.me/psyriotyk")]                         
                            ])
    #await message.answer( )
    await bot.send_message(chat_id=ID, text="<B>НАВИГАЦИЯ КАНАЛА👇</B>",reply_markup=main, parse_mode="HTML")

    
    

if __name__ == "__main__":
    asyncio.run(main())