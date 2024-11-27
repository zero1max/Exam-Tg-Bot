from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models.user import User
from keyboards.main import *

class UserState(StatesGroup):
    role = State()  # O'qituvchi yoki O'quvchi tanlash
    full_name = State()  # Foydalanuvchi ismini kiritish

router = Router()

@router.message(CommandStart())
async def register(msg: Message, state: FSMContext):
    user = await User.get_or_none(user_id = msg.from_user.id)
    if not user:
        await msg.answer("Siz avval ro'yxatdan o'tmagansiz! Iltimos avval ro'yxatdan o'ting!!!")
        await state.set_state(UserState.full_name)
        await msg.answer("FullName kiriting:")
    else:
        await msg.answer("Siz ro'yxatdan o'tgansiz")

@router.message(UserState.full_name)
async def get_fullname(msg: Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await state.set_state(UserState.role)
    await msg.answer("Tanlang:", reply_markup=register_role)

@router.message(UserState.role)
async def get_role(msg: Message, state: FSMContext):
    print(msg.text)