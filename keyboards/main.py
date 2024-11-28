from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

register_role = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Student"), KeyboardButton(text='Teacher')]
    ]
)

choice_teacher = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Dars yuklash"), KeyboardButton(text="Darslarni ko'rish")],
        [KeyboardButton(text="O'quvchilarni ko'rish")]
    ]
)

choice_student = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Darsliklarni ko'rish")]
    ]
)

def create_lessons_keyboard(lessons):
    """
    Darslar uchun inline klaviatura yaratadi.
    
    Args:
        lessons (list): Darslar ro'yxati, har bir elementda (id, title) bo'ladi.
        
    Returns:
        InlineKeyboardMarkup: Darslar uchun tayyor inline klaviatura.
    """
    buttons = []  # Tugmalar ro'yxati
    row = []  # Hozirgi qator uchun tugmalar

    for index, lesson in enumerate(lessons):
        button = InlineKeyboardButton(
            text=f"{lesson['title']}",  # Dars nomini chiqarish
            callback_data=f"lesson_{lesson['id']}"  # Darsning id sini callback_data sifatida berish
        )
        row.append(button)

        # Agar 2 tugma bo'lsa, yangi qatorga o'tish
        if len(row) == 2 or index == len(lessons) - 1:
            buttons.append(row)
            row = []  

    inline_kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return inline_kb