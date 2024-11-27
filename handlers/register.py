from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models.user import User
from keyboards.main import *
from services.user import *

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
    if user:
        await msg.answer("/check Buyrug'ini yuboring")

@router.message(UserState.full_name)
async def get_fullname(msg: Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await state.set_state(UserState.role)
    await msg.answer("Tanlang:", reply_markup=register_role)

@router.message(UserState.role)
async def get_role(msg: Message, state: FSMContext):
    await state.update_data(role=msg.text)
    
    data = await state.get_data()
    print(data)
    fullname = data["full_name"]
    if data['role'] == "Student":
        await add_user(user_id=msg.from_user.id, full_name=fullname, is_student=True, is_teacher=False)
        await msg.answer(f"{msg.from_user.full_name} Welcome! You have been successfully registered.")
        await msg.answer("/check Buyrug'ini yuboring")
    elif data["role"] == "Teacher":
        await add_user(user_id=msg.from_user.id, full_name=fullname, is_student=False, is_teacher=True)
        await msg.answer(f"{msg.from_user.full_name} Welcome! You have been successfully registered.")
        await msg.answer("/check Buyrug'ini yuboring")
