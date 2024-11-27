from models.user import User

async def get_user(user_id: int):
    user = await User.get_or_none(user_id=user_id)
    return user

