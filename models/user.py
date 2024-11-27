from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)  # Auto-increment primary key
    user_id = fields.BigIntField(unique=True)  # Telegram User ID
    full_name = fields.CharField(max_length=255)
    is_student = fields.BooleanField(default=False)
    is_teacher = fields.BooleanField(default=False)

    class Meta:
        table = "users"

    def __str__(self):
        return self.full_name

class Lesson(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    teacher = fields.ForeignKeyField('models.User', related_name='lessons', on_delete=fields.CASCADE)

    def __str__(self):
        return self.title


class Attendance(Model):
    id = fields.IntField(pk=True)
    lesson = fields.ForeignKeyField('models.Lesson', related_name='attendances', on_delete=fields.CASCADE)
    student = fields.ForeignKeyField('models.User', related_name='attendances', on_delete=fields.CASCADE)
    attended_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} attended {self.lesson.title}"

