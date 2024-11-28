from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from models.user import User
from services.user import *
from keyboards.main import *

class Lessons(StatesGroup):
    title = State()
    description = State()

router = Router()

@router.message(Command('check'))
async def start_msg(msg: Message):
    user = await User.get_or_none(user_id = msg.from_user.id)
    if user:
        information = await get_user(msg.from_user.id)
        if information.is_student:
            await msg.answer("Student Hi", reply_markup=choice_student)

        elif information.is_teacher:
            await msg.answer('Salom teacher', reply_markup=choice_teacher)


# --------------------------- Upload Lessons -------------------------------------
@router.message(F.text == "Dars yuklash")
async def teacher_yes(msg: Message, state: FSMContext):
    await state.set_state(Lessons.title)
    await msg.answer("Dars title ni kiriting")

@router.message(Lessons.title)
async def get_title(msg: Message, state: FSMContext):
    await state.update_data(title = msg.text)
    await state.set_state(Lessons.description)
    await msg.answer("Darslik description qismini yuboring")

@router.message(Lessons.description)
async def get_description(msg: Message, state: FSMContext):
    await state.update_data(description = msg.text)

    data = await state.get_data()
    await add_lesson(title=data['title'], description=data['description'], teacher_id=msg.from_user.id)
    await state.clear()
    await msg.answer("Yuklandi")

# --------------------------- See Lessons -------------------------------------
@router.message(F.text == "Darslarni ko'rish")
async def see_lessons(msg: Message):
    lessons = await saw_lessons()
    for lesson in lessons:
        await msg.answer(f"ID: {lesson.id}, Title: {lesson.title}, Description: {lesson.description}")

# --------------------------- See Lessons -------------------------------------
@router.message(F.text == "O'quvchilarni ko'rish")
async def see_students(msg: Message):
    students = await saw_students()
    for student in students:
        await msg.answer(f"ID: {student.id}, FullName: {student.full_name}")