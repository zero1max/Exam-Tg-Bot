from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models.user import User

class UserState(StatesGroup):
    role = State()  # O'qituvchi yoki O'quvchi tanlash
    full_name = State()  # Foydalanuvchi ismini kiritish

router = Router()

@router.message(CommandStart())
async def start_msg(msg: Message):
    await msg.answer("Assalomu aleykum!")