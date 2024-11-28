from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command
from services.user import *
from models.user import *
from keyboards.main import * 

router = Router()

@router.message(F.text == "Darsliklarni ko'rish")
async def show_lessons(msg: Message):
    # Darslar ro'yxatini olish, id va title maydonlari bilan
    lessons = await Lesson.all().values('id', 'title')  
    print(lessons)  # Konsolga chiqarish, keyinroq olib tashlash mumkin
    # Inline klaviatura yuborish
    await msg.answer("Tanlang: ", reply_markup=create_lessons_keyboard(lessons=lessons))