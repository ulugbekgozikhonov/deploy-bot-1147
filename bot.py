from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import logging

logging.basicConfig(level=logging.INFO)
from database import *
from state import RegisterState
from default_btn import *

BOT_TOKEN = "7066529744:AAF0geBN3EEmzjFG-FCQg28B6jwB9keJSOs"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)

async def on_startup(dp):
    create_tables()
    await bot.send_message(chat_id=909437832,text="Bot has strated")

@dp.message_handler(commands="start")
async def start_handler(message:types.Message,state:FSMContext):
    chat_id = message.chat.id
    user =  get_user_by_chat_id(chat_id=chat_id)
    if user is not None:
        await message.answer("Welcome to books shop",reply_markup=shop_menu)
    else:
        await message.answer("Welcome to books shop\nYou can register for use this bot")
        await message.answer("Enter full_name:")
        await state.update_data(chat_id=chat_id)
        await RegisterState.full_name.set()
    
    
        
@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message:types.Message,state:FSMContext):
    full_name = message.text
    await message.answer("Share Contact", reply_markup=phone_number)
    await state.update_data(full_name=full_name)
    await RegisterState.phone_number.set()

@dp.message_handler(state=RegisterState.phone_number,content_types=types.ContentType.CONTACT)
async def get_phone_number(message:types.Message,state:FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    if register_user(data=data):
        await message.answer("Successfully registreted\nYou can use this bot:",reply_markup=shop_menu)
        await state.finish()
    else:
        await message.answer("Register Error",reply_markup=ReplyKeyboardRemove())


@dp.message_handler(content_types="sticker")
async def sticker_handler(message:types.Message):
    await message.answer_sticker(message.sticker.file_id)
    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
