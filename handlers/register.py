from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class UserState(StatesGroup):
    role = State()  # O'qituvchi yoki O'quvchi tanlash
    full_name = State()  # Foydalanuvchi ismini kiritish

