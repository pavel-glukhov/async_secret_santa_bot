from tortoise.models import Model
from tortoise import fields


class User(Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(max_length=64)
    first_name = fields.CharField(max_length=64, null=True)
    last_name = fields.CharField(max_length=64, null=True)
    email = fields.CharField(max_length=64, null=True)
    address = fields.CharField(max_length=256, null=True)
    contact_number = fields.CharField(max_length=12, null=True)
    registered_at = fields.DatetimeField(auto_now_add=True)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)

    def __str__(self):
        return f"User {self.user_id} : {self.username}"


class Room(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=12, null=False)
    number = fields.IntField(null=False)
    budget = fields.CharField(max_length=12, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    is_started = fields.BooleanField(default=False)
    started_at = fields.DatetimeField(null=True)
    finished_at = fields.DatetimeField(null=True)
    owner = fields.ForeignKeyField('models.User', related_name='room_owner')
    members = fields.ManyToManyField('models.User', related_name='members',
                                     through='rooms_users', on_delete='CASCADE')


    def __str__(self):
        return f"Room {self.number}: {self.name}"


class Wish(Model):
    id = fields.IntField(pk=True)
    wish = fields.CharField(max_length=256, null=False)
    room = fields.ForeignKeyField('models.Room', related_name='room',
                                  on_delete='CASCADE')
    user = fields.ForeignKeyField('models.User', related_name='wishes_of_owner')

    def __str__(self):
        return f"Room {self.room}: {self.user}"


class GameResult(Model):
    id = fields.IntField(pk=True)
    room = fields.ForeignKeyField('models.Room', related_name='result_of_game')
    recipient = fields.ForeignKeyField('models.User', related_name='recipient')
    sender = fields.ForeignKeyField('models.User', related_name='sender')
    assigned_at = fields.DatetimeField(null=True)
