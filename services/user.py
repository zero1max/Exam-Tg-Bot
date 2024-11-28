from models.user import User, Lesson

async def add_user(user_id: int, full_name: str, is_student: bool, is_teacher: bool):
    if is_teacher == True:
        user = User(
        user_id=user_id,
        full_name=full_name,
        is_student=False,
        is_teacher=True)
    elif is_teacher == False:
        user = User(
        user_id=user_id,
        full_name=full_name,
        is_student=True,
        is_teacher=False)
        
    await user.save()

async def add_lesson(title: str, description: str, teacher_id: int):
    teacher = await User.get(user_id=teacher_id)
    lesson = Lesson(
        title=title,
        description=description,
        teacher=teacher
    )
    await lesson.save()

async def get_user(user_id: int):
    user = await User.get_or_none(user_id=user_id)
    return user


async def saw_lessons():
    lessons = await Lesson.all()
    return lessons


async def saw_students():
    students = await User.filter(is_student=True)
    return students