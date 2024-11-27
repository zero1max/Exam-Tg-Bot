from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models.user import User
from services.user import *

class UserState(StatesGroup):
    role = State()  # O'qituvchi yoki O'quvchi tanlash
    full_name = State()  # Foydalanuvchi ismini kiritish

router = Router()

@router.message(Command('check'))
async def start_msg(msg: Message):
    user = await User.get_or_none(user_id = msg.from_user.id)
    if user:
        information = await get_user(msg.from_user.id)
        if information.is_student:
            await msg.answer("Student Hi")
        elif information.is_teacher:
            await msg.answer('Salom teacher')
        print(information)
        # await msg.answer("Hi Bro")